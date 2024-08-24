from flask import Flask, render_template, jsonify
import psutil
import socket
import threading
import time
import getpass
from collections import deque

app = Flask(__name__)

# Use deque for thread-safe, fixed-size CPU history
cpu_usage_history = deque(maxlen=10)

def get_system_info():
    try:
        ip_address = socket.gethostbyname(socket.gethostname())
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.used / (1024 * 1024)  # Convert bytes to MB
        net_io = psutil.net_io_counters()
        net_stats = {
            'bytes_sent': net_io.bytes_sent / 1024,  # Convert to KB
            'bytes_recv': net_io.bytes_recv / 1024   # Convert to KB
        }
        return ip_address, cpu_usage, memory_usage, net_stats
    except Exception as e:
        print(f"Error getting system info: {e}")
        return "Unknown", 0, 0, {'bytes_sent': 0, 'bytes_recv': 0}

def collect_cpu_usage():
    while True:
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            cpu_usage_history.append(cpu_usage)
            time.sleep(1)
        except Exception as e:
            print(f"Error collecting CPU usage: {e}")

threading.Thread(target=collect_cpu_usage, daemon=True).start()

@app.route('/')
def index():
    try:
        user_name = getpass.getuser()  # Get the system user's name
        ip_address, cpu_usage, memory_usage, net_stats = get_system_info()
        return render_template('index.html', name=user_name, ip_address=ip_address, cpu_usage=cpu_usage, memory_usage=memory_usage, net_stats=net_stats)
    except Exception as e:
        print(f"Error in index route: {e}")
        return "Error loading page", 500

@app.route('/cpu_history')
def cpu_history():
    return jsonify(list(cpu_usage_history))

@app.route('/live_data')
def live_data():
    try:
        _, cpu_usage, memory_usage, net_stats = get_system_info()
        return jsonify({
            'cpu_usage': cpu_usage,
            'memory_usage': memory_usage,
            'net_stats': net_stats
        })
    except Exception as e:
        print(f"Error in live_data route: {e}")
        return jsonify({
            'cpu_usage': 0,
            'memory_usage': 0,
            'net_stats': {'bytes_sent': 0, 'bytes_recv': 0}
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # Enable debug mode for development
