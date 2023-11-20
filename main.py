from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

WIDTH =128 
HEIGHT= 64

i2c = I2C(0, scl = Pin(26), sda = Pin(27),  freq = 400000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
while True:
    oled.fill(0)
    oled.text("DIY PROJECTS LAB", 0, 0)
    oled.text("Tutorial", 0, 40)
    oled.show()