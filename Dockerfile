# Start with a lightweight Python 3.11 image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    supervisor \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip/setuptools/wheel
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Copy and install Python dependencies
COPY requirements.txt .

# Safety: uninstall conflicting packages before installing your known-good set
RUN pip uninstall -y langchain langchain-core langchain-community langgraph-prebuilt || true

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application source code
COPY . .

# Ensure Streamlit secrets file exists before build
RUN mkdir -p /app/.streamlit
COPY .streamlit/secrets.toml /app/.streamlit/secrets.toml

# Copy Supervisor configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose FastAPI + Streamlit + optional admin port
EXPOSE 8000 8501 8001

# Start Supervisor, which manages both FastAPI (Uvicorn) and Streamlit
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
