from machine import Pin
from time import sleep

led = Pin(26, Pin.OUT)

while True:
  led.on()
  sleep(0.5)
  led.off()
  sleep(0.5)
