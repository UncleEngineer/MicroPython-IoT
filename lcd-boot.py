from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
import time

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
#print(i2c.scan())
#print('Address: ', hex(i2c.scan()[0]))
lcd = I2cLcd(i2c, 0x3f, 2,16)
# String
#lcd.putstr('Hello World\nby Uncle')

# CHAR from ROM
#lcd.putchar(chr(126))

# Custom Char 0-7

a = '        Hello'
b = '   Hello World'

lcd.putstr(a)
time.sleep(2)
lcd.clear()
lcd.putstr(b)

'''
smile = bytearray([0x00,0x00,0x0A,0x00,0x00,0x11,0x0E,0x00])
angry =bytearray([0x00,0x11,0x0A,0x00,0x00,0x0E,0x11,0x00])

lcd.custom_char(0, smile)
lcd.custom_char(1, angry)

lcd.putchar(chr(0))
lcd.move_to(5,0) # move to column 2 row 0
lcd.putchar(chr(1))

lcd.blink_cursor_on()
time.sleep(5)
lcd.blink_cursor_off()
lcd.hide_cursor() # lcd.show_cursor()
'''

# display on/off
'''
time.sleep(2)
lcd.display_off()
time.sleep(2)
lcd.display_on()
'''

# backlight on/off
'''
for i in range(10):
    lcd.backlight_off()
    time.sleep(2)
    lcd.backlight_on()
    time.sleep(2)
'''

  
  
  
  
  
  
