# Use Node.js LTS version (Alpine)
FROM node:20-alpine

# Set working directory
WORKDIR /frontend

# Install required build tools (Alpine uses apk)
RUN apk add --no-cache curl build-base



# Copy package files
COPY package.json yarn.lock* package-lock.json* ./

# Install dependencies
RUN if [ -f yarn.lock ]; then yarn install --frozen-lockfile; \
    elif [ -f package-lock.json ]; then npm ci; \
    else npm install; fi

# Copy the rest of the application
COPY . .

# Expose port 5173 (Vite default)
EXPOSE 5173

# Start development server
CMD ["yarn", "dev", "--host", "0.0.0.0", "--port", "5173"]
