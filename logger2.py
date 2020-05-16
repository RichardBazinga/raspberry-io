import os
from time import sleep

while True:
  os.system("echo 'logger 2' > log.log")
  os.system("echo 'logger 2'")
  sleep(1)
