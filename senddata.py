import socket
import network
import time
from machine import Pin
#####################
# serverip = '178.128.125.82'
serverip = '192.168.0.100'
port = 9000
#####################

def send_data(data):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    server.connect((serverip,port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Server:' , data_server)
    server.close()

########WIFI########
wifi = 'Uncle Engineer(2.4GHz)'
password = '212224236'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(2) # delay 2 seconds
wlan.connect(wifi, password)
time.sleep(2)
print(wlan.isconnected())
####################

led = Pin(23, Pin.OUT)

for i in range(60):
    led.on()
    send_data('LED1:ON')
    time.sleep(2)
    led.off()
    send_data('LED1:OFF')
    time.sleep(2)
    
    
    




