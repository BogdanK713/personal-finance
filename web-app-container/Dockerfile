# Base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy files and install dependencies
COPY . .
RUN npm install && npm run build

# Install static file server
RUN npm install -g serve

# Expose port
EXPOSE 8080

# Start production server
CMD ["serve", "-s", "dist", "-l", "8080"]
