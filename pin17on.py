#!/urs/bin/env python3

from gpiozero import LED

led = LED(17)
os.system("Echo 'killing python'")
os.system("kill -9 `pgrep python`")
while True:
    led.on()