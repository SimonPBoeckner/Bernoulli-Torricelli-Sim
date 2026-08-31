import ignore.do as do
import queue
import time

buffer = queue.Queue(maxsize=50)
thread = do.Source(buffer, 10, 0.5, 5)

try:
    while True:
        data = buffer.get()

        if buffer.qsize() > 40:
            print(f"[Warning] Main thread falling behind! Buffer size: {buffer.qsize()}")

        time.sleep(0.01)

except KeyboardInterrupt:
    print("\nStopping sensor stream...")
    thread.join()
    print("Cleanly stopped.")