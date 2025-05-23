FROM python:3.10-slim

# Set the base working directory
WORKDIR /app

# Copy requirements file
COPY ./requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy application code and .env file
COPY ./app ./app


# Set working directory to the app code
WORKDIR /app/app

# Set PYTHONPATH so internal imports work
ENV PYTHONPATH=/app/app

# Expose gRPC port
EXPOSE 50051

# Run both the gRPC server and the health check
CMD ["sh", "-c", "python server.py & python health_check.py"]
