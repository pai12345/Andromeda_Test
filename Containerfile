# Python base image
FROM python:3.10.0a6-alpine3.13

# Create working directory
WORKDIR /app

# Copy requirements.txt to app
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy contents to app
COPY . .

# Expose Port
EXPOSE 8000

# Execute App
ENTRYPOINT [ "python", "index.py" ]  
