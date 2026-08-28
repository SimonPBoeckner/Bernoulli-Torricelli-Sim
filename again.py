import threading
import random

class DataSource(threading.Thread):

    def __init__(self, data_queue, hz=100, setpoint=1, error=0.1):
        super().__init__()
        self.setpoint = setpoint
        self.error = error
        self.interval = 1
        self._stop_event = threading.Event()

        self.start()

    def start(self, interval):
        self.interval = interval
        if self.is_alive():
            return
        print(f"[{self.name}] Started background loop (every {self.interval}s)")
        super().start()

    def run(self):
        while not self._stop_event.is_set():
            ret_val = self.setpoint + random.uniform(-self.error, self.error)
            self._stop_event.wait(self.interval)

    def stop(self):
        self._stop_event.set()
        self.
    