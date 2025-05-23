FROM python:3.10-slim

# Set the base working directory
WORKDIR /app

# Copy only the requirements file first (for better Docker caching)
COPY ./requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application code
COPY ./app ./app

# Set working directory to the app code
WORKDIR /app/app

# Set PYTHONPATH so internal imports work properly
ENV PYTHONPATH=/app/app

# Expose gRPC port
EXPOSE 50051

# Run the service
CMD ["python", "server.py"]
