# Base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Install dependencies first (layer caching)
COPY package*.json ./
RUN npm install

# Copy the rest of the files
COPY . .

# Build React app
RUN npm run build

# Install static file server
RUN npm install -g serve

# Expose internal port (ALWAYS 8080 inside container)
EXPOSE 8080

# Serve built app on internal port 8080
CMD ["serve", "-s", "dist", "-l", "8080"]
