#!/urs/bin/env python3
import os
from gpiozero import LED

led = LED(17)
os.system("Echo '...Running pin17on.py'")

while True:
    led.on()