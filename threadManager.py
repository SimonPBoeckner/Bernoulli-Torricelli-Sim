import threading
import time
import typing

def thread_print(string:str, delay:int=2):
    print(f"Thread {threading.current_thread().name}: {string}\nWaiting for {delay} seconds for a response")
    time.sleep(delay)
    print(f"Thread {threading.current_thread().name}: done waiting")


strings: typing.List[str] = [
    "hey",
    "hi",
    "hello",
]

i = 1
threads: typing.List[threading.Thread] = []
for string in strings:
    t = threading.Thread(name=str(i), target=thread_print, args=(string,), kwargs={"delay": 1})
    threads.append(t)
    i += 1

for t in threads:
    t.start()

for t in threads:
    t.join()