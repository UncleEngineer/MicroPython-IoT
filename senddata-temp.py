# senddata-temp.py
import socket
import network
import time
from machine import Pin
import dht
#####################
# serverip = '178.128.125.82'
serverip = '192.168.0.100'
port = 9001
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
print('STATUS:',wlan.isconnected())
####################


print('> Temperature cheking...')
d = dht.DHT22(Pin(23))


for i in range(50):
    d.measure() # ***
    time.sleep(1)
    temp = d.temperature()
    humid = d.humidity()
    print(temp)
    print(humid)
    # text = 'TEMP-HUMID:{} and {}'.format(temp,humid)
    text = 'TEMP:{}'.format(temp)
    send_data(text)
    time.sleep(3)
    print('------')

