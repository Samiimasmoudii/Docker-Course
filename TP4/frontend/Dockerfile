# Use the official Nginx image as a base
FROM nginx:alpine

# Copy the HTML file to the Nginx directory
COPY ./src /usr/share/nginx/html

# Expose port 80 (default for Nginx)
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
    