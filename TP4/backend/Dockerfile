# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file if you have one (e.g., requirements.txt)
# COPY requirements.txt ./

# Install Flask (you can also create a requirements.txt and copy it)
RUN pip install Flask
RUN pip install --break-system-packages Flask Flask-cors 




# Copy the backend source code into the container
COPY backend.py .

# Expose the port the app runs on
EXPOSE 5000

# Start the Flask application
CMD ["python", "backend.py"]
