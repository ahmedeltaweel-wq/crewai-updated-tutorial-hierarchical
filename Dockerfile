# Use Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY telegram_bot.py .
COPY company_knowledge.md .
COPY company_loader.py .
COPY knowledge_base.py .
COPY language_detector.py .
COPY response_formatter.py .

# Set environment variables (will be overridden by Cloud Run)
ENV TELEGRAM_BOT_TOKEN=""
ENV GEMINI_API_KEY=""

# Run the bot
CMD ["python", "telegram_bot.py"]
