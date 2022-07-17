from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
from lcd_api import LcdApi
import time

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)

#print(i2c.scan())
lcd = I2cLcd(i2c, 0x3f ,2,16)

'''
a = '           Hello'
b = '     Hello World'

lcd.putstr(a)
time.sleep(2)
lcd.clear()
lcd.putstr(b)
'''

korkai = bytearray([0x0E,0x11,0x09,0x11,0x11,0x11,0x11,0x11])
khorkhai = bytearray([0x1A,0x1A,0x0A,0x0A,0x0A,0x0A,0x0A,0x0E])


def sawatdee(start=0):
    c1 = bytearray([0x00,
      0x00,
      0x00,
      0x00,
      0x00,
      0x19,
      0x11,
      0x1E
    ])

    c2 = bytearray([0x00,
      0x00,
      0x00,
      0x00,
      0x00,
      0x0D,
      0x13,
      0x1F
    ])

    c3 = bytearray([0x01,
      0x1E,
      0x11,
      0x01,
      0x05,
      0x0B,
      0x11,
      0x11])

    c4 = bytearray([0x00,
      0x1F,
      0x11,
      0x01,
      0x01,
      0x01,
      0x03,
      0x03])

    c6 = bytearray([0x00,
      0x1F,
      0x11,
      0x1D,
      0x1D,
      0x15,
      0x19,
      0x11])

    lcd.custom_char(0, c1)
    lcd.custom_char(1, c2)
    lcd.custom_char(2, c3)
    lcd.custom_char(3, c4)
    lcd.custom_char(4, c6)

    lcd.move_to(start + 1,0)
    lcd.putchar(chr(0))
    lcd.move_to(start + 3,0)
    lcd.putchar(chr(1))
    lcd.move_to(start + 0,1)
    lcd.putchar(chr(2))
    lcd.putchar(chr(3))
    lcd.putchar(chr(2))
    lcd.putchar(chr(4))
    
sawatdee(6) 
#lcd.putstr('Uncle Engineer \n2022')
'''
lcd.putchar(chr(248))
lcd.move_to(2,1)
lcd.putchar(chr(244))
'''
'''
smile = bytearray([0x00,0x00,0x0A,0x00,0x00,0x11,0x0E,0x00])
uncle = bytearray([0x04,0x04,0x1F,0x00,0x00,0x1F,0x04,0x04])

lcd.custom_char(0, smile)
lcd.custom_char(1, uncle)

lcd.putchar(chr(0))
lcd.move_to(3,1)
lcd.putchar(chr(1))
'''

  
  
  
  
  
  
  
