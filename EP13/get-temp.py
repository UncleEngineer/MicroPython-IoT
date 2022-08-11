# get-temp.py
# PC ---> ESP32--(T,H)--> PC --> CSV --> GUI --> Table

import socket
import threading
import time
import csv
from datetime import datetime

def writecsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)


serverip = '192.168.0.197'
port = 80

def gettemp():
    while True:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        server.connect((serverip,port))
        server.send('PC|TEMP'.encode('utf-8'))
        data = server.recv(1024).decode('utf-8')
        server.close()

        stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # strftime.org
        print(data)
        t,h = data.split('_')
        dt = [stamp,t,h]
        writecsv(dt)
        time.sleep(10)

gettemp()
