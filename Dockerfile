# Start from the latest Python 3.9-alpine image
FROM python:3.9-alpine

# Install Chromium and its dependencies
RUN apk add --no-cache \
    chromium \
    chromium-chromedriver \
    && rm -rf /var/cache/apk/*

# Set the working directory in the container
WORKDIR /app

# Copy the Python code to the container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .

# Set the entrypoint command for the container
ENTRYPOINT ["/bin/sh"]
CMD ["python", "main.py"]
