# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY web_app.py .
COPY agents.py .
COPY tasks.py .
COPY file_io.py .

# Copy tools directory (CRITICAL FIX)
COPY tools/ tools/

# Handle templates
COPY index.html templates/index.html

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=web_app.py
ENV PORT=5000
ENV PYTHONPATH=/app

# Run the application
CMD ["python", "web_app.py"]
