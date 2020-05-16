#!/urs/bin/env python3
import os
from gpiozero import LED

led = LED(17)
os.system("echo '...Running pin17off.py'")

while True:
    led.off()