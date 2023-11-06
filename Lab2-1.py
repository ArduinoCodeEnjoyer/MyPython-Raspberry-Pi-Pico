from machine import Pin
import time


p21 = Pin(21, Pin.OUT)

while(1):
    p21.on()
    time.sleep_ms(1000)
    print("Check")
    p21.off()
    time.sleep_ms(500)
    print("Check")