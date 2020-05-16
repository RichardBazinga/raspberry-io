#!/urs/bin/env python3
import os
import sys
from gpiozero import LED
from time import sleep

led = LED(17)
os.system("echo '...Running pin17bkink.py'")

while True:
    led.on()
    sleep(float(sys.argv[1]))
    led.off()
    sleep(float(sys.argv[2]))


