# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the working directory
COPY iot-telemetry-sender.py .

# Install the required packages
RUN pip install --no-cache-dir websockets

# Expose the necessary port(s) for the application
EXPOSE 8765

# Start the application | Show IP Address
CMD ["sh", "-c", "echo -n 'Websocket Server IP:' && hostname -I | cut -d ' ' -f1 && python iot-telemetry-sender.py"]

