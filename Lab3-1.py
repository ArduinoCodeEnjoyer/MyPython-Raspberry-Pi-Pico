from machine import Pin
import time

#hex 0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7C, 0x07, 0x7F, 0x6F 

button = Pin(14, Pin.IN, Pin.PULL_UP)
led_num = (0x3F,0x06,0x5B, 0x4F,0x66,
                   0x6D,0x7D,0x07,0x7F,0x6F,
                   0x77,0x7C,0x39,0x5E,0x79,
                   0x71,0x80)
ledpin = (16, 17, 18, 19, 20, 21, 22)

for i in range(0, len(ledpin)):
    ledpin.append(Pin(ledpin[i], Pin.OUT))
    time.sleep_ms(500)
    
def display7seg(num):
    segment = led_num[num]
    for i in range(8):
        if segment & 0b1:
            led[i].on()
        else:
            led[i].off()
        segment >>= 1
        
i = 0

while True:
    if button.value() == 0:
        display7seg(i)
        time.sleep_ms(250)
        i += 1
        if i > 15:
            i=0