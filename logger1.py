import os
from time import sleep

while True:
  os.system("echo 'logger 1' >> log.log")
  os.system("echo 'logger 1'")
  sleep(1)
