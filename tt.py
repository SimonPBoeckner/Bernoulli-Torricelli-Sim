import threading
import queue
import time
import random

def sensor_reader(data_queue, stop_event, hz=100):
    """Simulates a sensor reading exactly at the target HZ rate."""
    interval = 1.0 / hz  # 0.01 seconds for 100Hz
    
    # Align the start time
    next_time = time.perf_counter()
    samples_generated = 0
    
    print(f"[Sensor] Starting 100Hz polling loop...")
    
    while not stop_event.is_set():
        # 1. Simulate the sensor hardware read
        timestamp = time.time()
        voltage_reading = random.uniform(3.2, 3.4)  # Mock sensor payload
        sensor_data = {"time": timestamp, "value": voltage_reading}
        
        # 2. Push to queue. block=False prevents the 100Hz loop from lagging 
        # if the consumer falls behind. Instead, it drops or handles overflow.
        try:
            data_queue.put(sensor_data, block=False)
        except queue.Full:
            # Handle buffer overflow (backpressure strategy)
            pass 
        
        samples_generated += 1
        
        # 3. Calculate dynamic sleep to correct timing drift
        next_time += interval
        sleep_time = next_time - time.perf_counter()
        
        if sleep_time > 0:
            time.sleep(sleep_time)
        else:
            # If sleep_time is negative, the code is running too slow to maintain 100Hz
            # Reset next_time to current time to prevent a cascading catch-up loop
            next_time = time.perf_counter()

# Configuration
# Max size limits memory. At 100Hz, a maxsize of 50 holds 0.5 seconds of buffer.
sensor_buffer = queue.Queue(maxsize=50)
stop_signal = threading.Event()

# Start Thread
sensor_thread = threading.Thread(
    target=sensor_reader, 
    args=(sensor_buffer, stop_signal, 100), 
    daemon=True
)
sensor_thread.start()

# Main Thread Consumer
try:
    print("Main thread reading sensor stream. Press Ctrl+C to stop.")
    while True:
        # Batch process readings or handle them as they arrive
        data = sensor_buffer.get()
        
        # Process data (keep this lightweight or offload it to avoid buffer bloat)
        if sensor_buffer.qsize() > 40:
            print(f"[Warning] Main thread falling behind! Buffer size: {sensor_buffer.qsize()}")
            
        time.sleep(0.01) # Match the speed to consume normally
        
except KeyboardInterrupt:
    print("\nStopping sensor stream...")
    stop_signal.set()
    sensor_thread.join()
    print("Cleanly stopped.")
