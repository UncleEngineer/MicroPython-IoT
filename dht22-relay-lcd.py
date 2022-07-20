from machine import Pin, SoftI2C
from i2c_lcd import I2cLcd
from lcd_api import LcdApi
import time
import dht

# DEFINE RELAY
relay = Pin(19,Pin.OUT)
relay.value(1) #TURN OFF

def relay_on():
    relay.value(0)
    print('Relay: ON')
    
def relay_off():
    relay.value(1)
    print('Relay: OFF')
    

# DEFINE TEMP & HUMID
d = dht.DHT22(Pin(23))
time.sleep(2)

def get_temp_humid():
    d.measure()
    time.sleep(1)
    temp = d.temperature()
    humid = d.humidity()
    text_temp = 'TEMP: {:.1f} C'.format(temp)
    text_humid = 'HUMID: {:.1f} %'.format(humid)
    return (text_temp, text_humid, temp, humid)
    
#tp, th, t, h = get_temp_humid()
#print(tp)
#print(th)


# DEFINE LCD
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
lcd = I2cLcd(i2c, 0x3f, 2, 16)

def show_lcd(line1, line2):
    lcd.clear()
    lcd.putstr(line1)
    lcd.move_to(0,1) # lcd.move_to(COLUMN, ROW)
    lcd.putstr(line2)

while True:
    tp, th, t, h = get_temp_humid()
    show_lcd(tp,th)
    if t > 30:
        relay_on()
    else:
        relay_off()
    time.sleep(2)
    

