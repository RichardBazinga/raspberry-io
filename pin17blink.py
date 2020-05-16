#!/urs/bin/env python3
import os
from gpiozero import LED
from time import sleep

led = LED(17)
os.system("Echo 'killing python'")
os.system("kill -9 `pgrep python`")
while True:
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.15)


