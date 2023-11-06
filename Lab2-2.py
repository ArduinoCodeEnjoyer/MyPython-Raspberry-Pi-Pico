from machine import Pin
import time


p21 = Pin(21, Pin.OUT)
p20 = Pin(20, Pin.OUT)
p19 = Pin(19, Pin.OUT)
p18 = Pin(18, Pin.OUT)

while True:
    for i in range(0,5,1):
        p21.on()
        time.sleep_ms(50)
        p20.on()
        time.sleep_ms(50)
        p19.on()
        time.sleep_ms(50)
        p18.on()
        time.sleep_ms(1000)
    
        p21.off()
        time.sleep_ms(50)
        p20.off()
        time.sleep_ms(50)
        p19.off()
        time.sleep_ms(50)
        p18.off()
        time.sleep_ms(1000)
    time.sleep_ms(1000)
    
    for i in range(0,5,1):
        p21.on()
        time.sleep_ms(100)
        p21.off()
        p20.on()
        time.sleep_ms(100)
        p20.off()
        p19.on()
        time.sleep_ms(100)
        p19.off()
        p18.on()
        time.sleep_ms(100)
        p18.off()
        time.sleep_ms(100)
        
    time.sleep_ms(1000)
    
    for i in range(0,5,1):
        p21.on()
        time.sleep_ms(100)
        p21.off()
        time.sleep_ms(100)
        p20.on()
        time.sleep_ms(100)
        p20.off()
        time.sleep_ms(100)
        p19.on()
        time.sleep_ms(100)
        p19.off()
        time.sleep_ms(100)
        p18.on()
        time.sleep_ms(100)
        p18.off()
        time.sleep_ms(100)