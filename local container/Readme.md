
```docker build -t iot-telemetry-sender .```


```docker run --name iot-telemetry-sender -d -p 8765:8765 iot-telemetry-sender```



The code you provided is a Python script that generates random telemetry data (temperature and humidity) for an IoT device and sends it over a WebSocket connection using the websockets library. It listens on the "localhost" address and port 8765.

To run this code in a Docker container, you can follow these steps:

1. Create a Dockerfile: Use a text editor to create a file named "Dockerfile" (without any file extension) in the same directory as your Python script.

2. Add the Dockerfile content: Copy and paste the following content into the Dockerfile:

```Dockerfile
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

# Start the application
CMD ["python", "iot-telemetry-sender.py"]
```

3. Build the Docker image: Open a terminal or command prompt, navigate to the directory where the Dockerfile and Python script are located, and run the following command to build the Docker image:

```
docker build -t iot-telemetry-sender .
```

4. Run the Docker container: Once the image is built, you can start a container from it using the following command:

```
docker run -p 8765:8765 iot-telemetry-sender
```

The `-p 8765:8765` option maps the container's port 8765 to the host's port 8765, allowing you to access the WebSocket server running inside the container from your host machine.

Now, the Docker container should be running, and you can connect to the WebSocket server at `ws://localhost:8765` to receive the generated telemetry data.

Docker Image
![iot-telemetry-sender-image](https://github.com/expertcloudconsultant/iot-programme/assets/69172523/45e77ac9-db95-497d-bc09-77d2e523586c)

Running Container

![iot-telemetry-sender](https://github.com/expertcloudconsultant/iot-programme/assets/69172523/0eaa5b3d-9823-4203-859f-42c4e9714177)

Websocket Client
![iot-telemetry-sender-websocket-client](https://github.com/expertcloudconsultant/iot-programme/assets/69172523/1e8aadd1-cffb-419e-b669-c8730033e4f9)

Visualisation - Web Charts
![iot-telemetry-sender-visualisation](https://github.com/expertcloudconsultant/iot-programme/assets/69172523/408cbdcb-8ce4-42fb-9a0f-368eb4ace2bc)
