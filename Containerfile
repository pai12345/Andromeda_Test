# Python base image
FROM python:latest

# Create working directory
WORKDIR /app

# Copy requirements.txt to app
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy contents to app
COPY . .

# Expose Port
EXPOSE 5001

# Execute App
ENTRYPOINT [ "python", "index.py" ]  
