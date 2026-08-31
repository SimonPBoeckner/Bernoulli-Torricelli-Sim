import random
import threading
import os
import subprocess
import time
import shutil

class DataSource(threading.Thread):

    def __init__(self, setpoint, error, hz=100, autostart=True):
        super().__init__()
        self.setpoint = setpoint
        self.error = error
        self.interval = 1.0 / hz

        next_time = time.perf_counter()
        samples_gen
        self._stop_event = threading.Event()
        self.pipe = None
        self.pipe_path = f"/tmp/thread_{self.name}_pipe"

        if self._can_use_xterm():
            self._open_terminal_pipe()
        else:
            print("xterm is not available here; writing DataSource output in this terminal.")

        if autostart:
            self.start()

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
            print("xterm did not connect to the pipe; writing DataSource output in this terminal.")
            os.remove(self.pipe_path)
            return

        self.pipe = os.fdopen(pipe_fd, "w")
        os.remove(self.pipe_path)
        self._write(f"=== Window started for {self.name} ===")

    def _can_use_xterm(self):
        return bool(os.environ.get("DISPLAY")) and shutil.which("xterm") is not None

    def start(self):
        if self.is_alive():
            return
        print(f"[{self.name}] Started background loop (every {self.interval}s)")
        super().start()

    def run(self):
        while not self._stop_event.is_set():
            ret_val = self.setpoint + random.uniform(-self.error, self.error)
            self._write(f"[{self.name}] {ret_val}")
            self._stop_event.wait(self.interval)

    def stop(self):
        self._stop_event.set()
        self._write("=== Thread Finished ===")
        if self.pipe:
            self.pipe.close()

    def _write(self, message):
        if self.pipe:
            self.pipe.write(f"{message}\n")
            self.pipe.flush()
        else:
            print(message)
