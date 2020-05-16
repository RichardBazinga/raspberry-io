#!/urs/bin/env python3
import os
import sys
from gpiozero import LED
from time import sleep

print sys.argv[0] # prints python_script.py
print sys.argv[1] # prints var1
print sys.argv[2] # prints var2

led = LED(17)
os.system("echo '...Running pin17bkink.py'")

while True:
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.15)


