"""
Smart Document Management System with AI Chatbot
نظام إدارة مستندات ذكي مع شات بوت AI
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import json
import sqlite3
from datetime import datetime
import hashlib
from pathlib import Path
import mimetypes
import PyPDF2
import docx
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'jpg', 'jpeg', 'png', 'gif', 'zip', 'rar'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configure Gemini AI - Support both API Key and Vertex AI
api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
use_vertex_ai = os.getenv('USE_VERTEX_AI', 'false').lower() == 'true'
model = None

if api_key and not use_vertex_ai:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        print("✅ AI Model: gemini-1.5-flash (API Key)")
    except Exception as e:
        print(f"❌ AI Error: {e}")
elif use_vertex_ai or os.getenv('GOOGLE_CLOUD_PROJECT'):
    try:
        from vertexai.preview.generative_models import GenerativeModel
        import vertexai
        project_id = os.getenv('GOOGLE_CLOUD_PROJECT', 'eg-konecta-sandbox')
        location = os.getenv('VERTEX_AI_LOCATION', 'us-central1')
        vertexai.init(project=project_id, location=location)
        model = GenerativeModel('gemini-1.5-flash')
        print(f"✅ AI Model: Vertex AI gemini-1.5-flash ({project_id}/{location})")
    except Exception as e:
        print(f"❌ Vertex AI Error: {e}")
else:
    print("⚠️  No AI configured - set GEMINI_API_KEY or USE_VERTEX_AI=true")

# Database initialization
def init_db():
    conn = sqlite3.connect('smart_dms.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS files
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  filename TEXT NOT NULL,
                  original_filename TEXT NOT NULL,
                  file_path TEXT NOT NULL,
                  file_size INTEGER,
                  file_type TEXT,
                  upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  description TEXT,
                  tags TEXT,
                  content_text TEXT,
                  file_hash TEXT UNIQUE)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS chat_history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_message TEXT NOT NULL,
                  bot_response TEXT NOT NULL,
                  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  related_files TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS notes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  content TEXT NOT NULL,
                  created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  related_files TEXT,
                  tags TEXT)''')
    
    conn.commit()
    conn.close()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def get_file_hash(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def extract_text_from_file(file_path, file_type):
    try:
        if file_type == 'txt':
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        elif file_type == 'pdf':
            text = ""
            with open(file_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                for page in pdf_reader.pages:
                    text += page.extract_text()
            return text
        elif file_type in ['doc', 'docx']:
            doc = docx.Document(file_path)
            return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        else:
            return ""
    except Exception as e:
        print(f"Extract error: {e}")
        return ""

def search_in_database(query, search_type='keyword'):
    conn = sqlite3.connect('smart_dms.db')
    c = conn.cursor()
    
    if search_type == 'keyword':
        pattern = f"%{query}%"
        c.execute('''SELECT id, filename, original_filename, file_type, file_size, upload_date, description, tags
                     FROM files 
                     WHERE original_filename LIKE ? OR description LIKE ? OR tags LIKE ? OR content_text LIKE ?
                     ORDER BY upload_date DESC''', 
                  (pattern, pattern, pattern, pattern))
    else:
        c.execute('SELECT id, filename, original_filename, file_type, file_size, upload_date, description, tags FROM files ORDER BY upload_date DESC')
    
    results = c.fetchall()
    conn.close()
    
    files = []
    for row in results:
        files.append({
            'id': row[0],
            'filename': row[2],
            'type': row[3],
            'size': row[4],
            'upload_date': row[5],
            'description': row[6] or '',
            'tags': row[7] or ''
        })
    
    return files

def ai_chat_response(user_message, context_files=None):
    if not model:
        return "AI غير متصل. أضف GEMINI_API_KEY في .env"
    
    try:
        context = "You are an intelligent assistant. Answer in Arabic or English based on user's language.\n\n"
        if context_files:
            context += "Documents:\n"
            for file in context_files[:3]:
                context += f"- {file['filename']}\n"
        context += f"\nUser: {user_message}"
        
        response = model.generate_content(context)
        return response.text
    except Exception as e:
        return f"AI Error: {str(e)}"

# Routes
@app.route('/')
def index():
    return render_template('smart_dms_index.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file'}), 400
    
    if file and allowed_file(file.filename):
        original_filename = secure_filename(file.filename)
        file_ext = original_filename.rsplit('.', 1)[1].lower()
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{timestamp}_{original_filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        file.save(file_path)
        
        file_size = os.path.getsize(file_path)
        file_hash = get_file_hash(file_path)
        content_text = extract_text_from_file(file_path, file_ext)
        
        description = request.form.get('description', '')
        tags = request.form.get('tags', '')
        
        try:
            conn = sqlite3.connect('smart_dms.db')
            c = conn.cursor()
            c.execute('''INSERT INTO files 
                         (filename, original_filename, file_path, file_size, file_type, description, tags, content_text, file_hash)
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                      (filename, original_filename, file_path, file_size, file_ext, description, tags, content_text, file_hash))
            conn.commit()
            file_id = c.lastrowid
            conn.close()
            
            return jsonify({'success': True, 'file_id': file_id, 'filename': original_filename})
        except sqlite3.IntegrityError:
            os.remove(file_path)
            return jsonify({'error': 'File exists'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/api/files', methods=['GET'])
def get_files():
    conn = sqlite3.connect('smart_dms.db')
    c = conn.cursor()
    c.execute('''SELECT id, original_filename, file_type, file_size, upload_date, last_modified, description, tags 
                 FROM files ORDER BY upload_date DESC''')
    
    files = []
    for row in c.fetchall():
        files.append({
            'id': row[0],
            'filename': row[1],
            'type': row[2],
            'size': row[3],
            'upload_date': row[4],
            'last_modified': row[5],
            'description': row[6],
            'tags': row[7]
        })
    
    conn.close()
    return jsonify(files)

@app.route('/api/files/<int:file_id>', methods=['DELETE'])
def delete_file(file_id):
    conn = sqlite3.connect('smart_dms.db')
    c = conn.cursor()
    c.execute('SELECT file_path FROM files WHERE id = ?', (file_id,))
    result = c.fetchone()
    
    if result:
        file_path = result[0]
        c.execute('DELETE FROM files WHERE id = ?', (file_id,))
        conn.commit()
        if os.path.exists(file_path):
            os.remove(file_path)
        conn.close()
        return jsonify({'success': True})
    
    conn.close()
    return jsonify({'error': 'Not found'}), 404

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query', '')
    search_type = data.get('type', 'keyword')
    results = search_in_database(query, search_type)
    return jsonify(results)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'No message'}), 400
    
    relevant_files = search_in_database(user_message, 'keyword')
    bot_response = ai_chat_response(user_message, relevant_files)
    
    conn = sqlite3.connect('smart_dms.db')
    c = conn.cursor()
    related_files_json = json.dumps([f['id'] for f in relevant_files[:5]])
    c.execute('INSERT INTO chat_history (user_message, bot_response, related_files) VALUES (?, ?, ?)',
              (user_message, bot_response, related_files_json))
    conn.commit()
    conn.close()
    
    return jsonify({'response': bot_response, 'relevant_files': relevant_files[:5]})

@app.route('/api/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'GET':
        conn = sqlite3.connect('smart_dms.db')
        c = conn.cursor()
        c.execute('SELECT id, title, content, created_date, last_modified, tags FROM notes ORDER BY last_modified DESC')
        
        notes_list = []
        for row in c.fetchall():
            notes_list.append({
                'id': row[0],
                'title': row[1],
                'content': row[2],
                'created_date': row[3],
                'last_modified': row[4],
                'tags': row[5]
            })
        
        conn.close()
        return jsonify(notes_list)
    
    elif request.method == 'POST':
        data = request.json
        title = data.get('title', '')
        content = data.get('content', '')
        tags = data.get('tags', '')
        
        conn = sqlite3.connect('smart_dms.db')
        c = conn.cursor()
        c.execute('INSERT INTO notes (title, content, tags) VALUES (?, ?, ?)', (title, content, tags))
        conn.commit()
        note_id = c.lastrowid
        conn.close()
        
        return jsonify({'success': True, 'note_id': note_id})

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    conn = sqlite3.connect('smart_dms.db')
    c = conn.cursor()
    c.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/notes/<int:note_id>/enhance', methods=['POST'])
def enhance_note(note_id):
    """AI-powered professional note enhancement in both languages"""
    if not model:
        return jsonify({'error': 'AI not configured'}), 503

    conn = sqlite3.connect('smart_dms.db')
    c = conn.cursor()
    c.execute('SELECT title, content FROM notes WHERE id = ?', (note_id,))
    result = c.fetchone()
    conn.close()

    if not result:
        return jsonify({'error': 'Note not found'}), 404

    title, content = result
    
    try:
        prompt = f"""You are a professional writing assistant. Enhance this note into TWO versions (Arabic & English).

Make it:
- Professional and eloquent
- Well-structured with clear paragraphs
- Grammatically perfect
- Detailed and comprehensive

Original Title: {title}
Original Content: {content}

Provide:
1. Enhanced ARABIC version (احترافي وبليغ)
2. Enhanced ENGLISH version (professional & eloquent)

Format:
[ARABIC]
<enhanced arabic content>

[ENGLISH]
<enhanced english content>
"""
        
        response = model.generate_content(prompt)
        enhanced_text = response.text
        
        # Extract sections
        arabic_section = ""
        english_section = ""
        
        if "[ARABIC]" in enhanced_text and "[ENGLISH]" in enhanced_text:
            parts = enhanced_text.split("[ENGLISH]")
            arabic_section = parts[0].replace("[ARABIC]", "").strip()
            english_section = parts[1].strip() if len(parts) > 1 else ""
        else:
            arabic_section = enhanced_text
            english_section = enhanced_text
        
        return jsonify({
            'success': True,
            'enhanced_arabic': arabic_section,
            'enhanced_english': english_section,
            'original_title': title
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/files/<int:file_id>/summarize', methods=['POST'])
def summarize_file(file_id):
    """AI file summarization in both languages"""
    if not model:
        return jsonify({'error': 'AI not configured'}), 503

    conn = sqlite3.connect('smart_dms.db')
    c = conn.cursor()
    c.execute('SELECT original_filename, content_text FROM files WHERE id = ?', (file_id,))
    result = c.fetchone()
    conn.close()

    if not result:
        return jsonify({'error': 'File not found'}), 404

    filename, content = result
    
    if not content:
        return jsonify({'error': 'No text content'}), 400

    try:
        preview = content[:8000]
        prompt = f"""Professional summary of document '{filename}' in BOTH languages.

Requirements:
- Provide summary in Arabic and English
- Be professional and eloquent
- Highlight key points
- Max 250 words per language

Document:
{preview}

Format:
[ARABIC SUMMARY]
<summary in Arabic>

[ENGLISH SUMMARY]
<summary in English>
"""
        
        response = model.generate_content(prompt)
        return jsonify({'success': True, 'summary': response.text, 'filename': filename})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 8080))
    print("🚀 Smart DMS Starting...")
    print(f"📁 Uploads: {app.config['UPLOAD_FOLDER']}")
    print(f"🤖 AI: {'Enabled ✅' if model else 'Disabled ❌'}")
    print(f"📡 Open your browser at: http://localhost:{port}")
    app.run(debug=False, host='0.0.0.0', port=port)
