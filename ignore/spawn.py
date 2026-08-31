import os
import subprocess
import threading
import time

def terminal_thread_linux(thread_name):
    # 1. Create a unique named pipe
    pipe_path = f"/tmp/thread_{thread_name}_pipe"
    if not os.path.exists(pipe_path):
        os.mkfifo(pipe_path)

    try:
        # 2. Spawn a new terminal window that reads from the pipe
        # Change 'xterm' to 'gnome-terminal --', 'konsole -e', etc., depending on your OS
        subprocess.Popen(['xterm', '-e', f'cat {pipe_path}'])
        
        # Give the terminal a split second to open and bind to the pipe
        time.sleep(0.5)

        # 3. Open the pipe for writing and send output
        with open(pipe_path, 'w') as pipe:
            pipe.write(f"=== Window started for {thread_name} ===\n")
            pipe.flush()
            
            for i in range(1, 6):
                pipe.write(f"[{thread_name}] Output line {i}\n")
                pipe.flush()  # Crucial: flush immediately so it appears live
                time.sleep(1)
                
            pipe.write("=== Thread Finished. Press Enter to close. ===\n")
            pipe.flush()

    finally:
        # Clean up the pipe when done
        os.remove(pipe_path)

# Start the thread
t = threading.Thread(target=terminal_thread_linux, args=("Worker-1",))
t.start()
