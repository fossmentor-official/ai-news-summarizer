# Use official Python base
FROM mcr.microsoft.com/devcontainers/python:3.10

# Set working directory
WORKDIR /workspace

# Copy requirements first (for layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . /workspace

# Expose app port
EXPOSE 8080

# Default command (Streamlit interface)
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
