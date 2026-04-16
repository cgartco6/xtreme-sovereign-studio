# Use a high-performance Python base
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Sovereign Engine files
COPY . .

# Expose the API port
EXPOSE 5000

# Fire it up
CMD ["python", "main.py"]
