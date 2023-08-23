import subprocess
from os import path
import os

subprocess.Popen(["pythonw", path.join(path.dirname(__file__), "set_black.py")])
