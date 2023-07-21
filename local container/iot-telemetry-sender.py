import json
import random
import asyncio
import websockets

device_id = "iot-device"

async def send_telemetry(websocket, path):
    while True:
        temperature = round(random.uniform(0, 50), 2)
        humidity = round(random.uniform(0, 100), 2)

        data = {
            "device_id": device_id,
            "temperature": temperature,
            "humidity": humidity
        }

        json_data = json.dumps(data)
        await websocket.send(json_data)

        await asyncio.sleep(1)  # Wait for 1 second before generating the next telemetry data

start_server = websockets.serve(send_telemetry, "0.0.0.0", 8765) # stands up a websocket

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
