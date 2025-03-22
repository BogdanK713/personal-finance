# Dockerfile for Transaction Service

FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Now copy the rest of the app
COPY . .

# Expose gRPC default port
EXPOSE 50051

# Start the gRPC server
CMD ["python", "transaction_service/app/server.py"]
