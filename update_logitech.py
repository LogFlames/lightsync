from logipy import logi_led

import os
import time
import ctypes

PATH = "C:/Users/Elias Lundell/code/lightsync/cycle.txt"

logi_led.logi_led_init()
time.sleep(1)

color = (0, 100, 100)

# Read file
while True:
    try:
        time.sleep(1)
        if not os.path.exists(PATH):
            break
        with open(PATH, "r") as f:
            cycle = int(f.read().strip())
        per = cycle / 3
        logi_led.logi_led_set_lighting(int(color[0] * per), int(color[1] * per), int(color[2] * per))
    except ValueError:
        break
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
        break

logi_led.logi_led_shutdown()
