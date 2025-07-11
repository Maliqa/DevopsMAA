```python
import psutil
import time

def monitor_system():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        print("-----------------------")
        time.sleep(2)

if __name__ == "__main__":
    monitor_system()
