# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Streamlit configuration
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLECORS=false
ENV STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false

# Run Streamlit
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.address=0.0.0.0"]