import os
from os import path
import signal
import subprocess

if path.exists("pid_set_black.txt"):
    subprocess.Popen(["pythonw", path.join(path.dirname(__file__), "kill_black.py")])
else:
    subprocess.Popen(["pythonw", path.join(path.dirname(__file__), "set_black.py")])

