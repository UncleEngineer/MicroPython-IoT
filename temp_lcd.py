from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
from lcd_api import LcdApi
import time
import dht

###################
high = bytearray([0x0E,
  0x11,
  0x1F,
  0x0E,
  0x0E,
  0x0E,
  0x0E,
  0x0E])

medium = bytearray([ 0x0E,
  0x11,
  0x11,
  0x0A,
  0x0E,
  0x0E,
  0x0E,
  0x0E
  ])

low = bytearray([ 0x0E,
  0x11,
  0x11,
  0x0A,
  0x0A,
  0x0A,
  0x0E,
  0x0E
  ])

lcd.custom_char(0, high)
lcd.custom_char(1, medium)
lcd.custom_char(2, low)


###################

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
lcd = I2cLcd(i2c, 0x3f ,2,16)

d = dht.DHT22(Pin(23))
r = Pin(19, Pin.OUT)
r.value(1)

d.measure()
time.sleep(1)
print(d.temperature())
print(d.humidity())

def gettemp():
    d.measure()
    time.sleep(1)
    temp = d.temperature()
    humid = d.humidity()
    text_temp = 'TEMP: {:.1f} C'.format(temp)
    text_humid = 'HUMID: {:.1f} %'.format(humid)
    return (text_temp, text_humid, temp, humid)

for i in range(100):
    temperature, humidity, temp, humid  = gettemp()
    lcd.backlight_on()
    lcd.clear() # clear screen
    lcd.putstr(temperature)
    lcd.move_to(0,1) # move to line 2
    lcd.putstr(humidity)
    time.sleep(2)
    
    if temp > 30:
        lcd.backlight_off()
        time.sleep(0.5)
        lcd.backlight_on()
        time.sleep(0.5)
        lcd.backlight_off()
        time.sleep(0.5)
    
    if temp > 30:
        r.value(0) # turn on relay
    else:
        r.value(1)
    
    if temp > 30:
        
        lcd.move_to(14,0)
        lcd.putchar(chr(0))
    elif temp > 28:
        
        lcd.move_to(14,0)
        lcd.putchar(chr(1))
    else:
        
        lcd.move_to(14,0)
        lcd.putchar(chr(2))
        
    
