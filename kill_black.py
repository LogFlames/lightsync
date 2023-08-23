import os
from os import path
import signal

pid_file = path.join(path.dirname(__file__), "pid_set_black.txt")

if os.path.exists(pid_file):
    with open(pid_file, "r") as f:
        pid = int(f.read().strip())
    try:
        os.kill(pid, signal.SIGTERM)
    except OSError:
        print("OSError, probably off-sync")
    os.remove(pid_file)
