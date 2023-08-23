from logipy import logi_led

from os import path
import time
import os

pid_file = path.join(path.dirname(__file__), "pid_set_black.txt")


if os.path.exists(pid_file):
    print("Cannot start while a process is already running")
    exit()

with open(pid_file, "w+") as f:
    f.write(str(os.getpid()))

logi_led.logi_led_init()
logi_led.logi_led_set_lighting(0, 0, 0)

try:
    time.sleep(3600 * 24)
except:
    pass

logi_led.logi_led_shutdown()
