import threading
import time
import random
import queue
import subprocess
import os


class Source(threading.Thread):

    def __init__(self, data_queue: queue.Queue, setpoint, error, hz=100, visualize=True):
        super().__init__()

        self.data_queue = data_queue
        self.setpoint = setpoint
        self.error = error
        self.interval = 1.0 / hz
        self.next_time = time.perf_counter()
        self._stop_event = threading.Event()
        self.pipe = None
        self.pipe_path = f"/tmp/thread_{self.name}_pipe"

        self._open_terminal_pipe()
        if visualize:
            self._graph()
        self.start()

    def start(self):
        if self.is_alive():
            return
        print(f"[{self.name}] Started background loop (every {self.interval:.4f}s)")
        super().start()

    def run(self):
        while not self._stop_event.is_set():
            timestamp = time.time()
            ret_val = self._generate_value()
            data = {"time": timestamp, "value": ret_val}

            if self.data_queue.full():
                self.data_queue.get()
            self.data_queue.put(data)

            self._write(f"[{self.name}] {ret_val}")

            self.next_time += self.interval
            sleep_time = self.next_time - time.perf_counter()

            if sleep_time > 0:
                time.sleep(sleep_time)
            else:
                self.next_time = time.perf_counter()

    def stop(self):
        self._stop_event.set()
        self._write("=== Thread Finished ===")
        if self.pipe:
            self.pipe.close()

    def _generate_value(self) -> float:
        return self.setpoint + random.uniform(-self.error, self.error)

    def _write(self, message):
        if self.pipe:
            self.pipe.write(f"[{message}]\n")
            self.pipe.flush()
        else:
            print(message)

    def _open_terminal_pipe(self):
        if os.path.exists(self.pipe_path):
            os.remove(self.pipe_path)
        os.mkfifo(self.pipe_path)

        subprocess.Popen(["xterm", "-e", "cat", self.pipe_path])
        deadline = time.time() + 3
        pipe_fd = None
        while pipe_fd is None and time.time() < deadline:
            try:
                pipe_fd = os.open(self.pipe_path, os.O_WRONLY | os.O_NONBLOCK)
            except OSError:
                time.sleep(0.1)

        if pipe_fd is None:
            print("xterm did not connect to the pipe; writing DataSource output to this terminal.")
            os.remove(self.pipe_path)
            return

        self.pipe = os.fdopen(pipe_fd, "w")
        os.remove(self.pipe_path)
        self._write(f"=== Window started for {self.name} ===")

    def _graph(self):
        pass