import socket
import threading
import time

serverip = '192.168.0.197'
port = 80

def send_data():
    for i in range(100):
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        server.connect((serverip,port))
        server.send('GUI-TEMP'.encode('utf-8'))
        data_server = server.recv(1024).decode('utf-8')
        print('Server:' , data_server)
        server.close()
        
        data_split = data_server.split('_')
        try:
            print('{} อุณหภูมิ {}'.format(data_split[0],data_split[1]))
        except:
            pass
        time.sleep(10)

def run_thread():
    task = threading.Thread(target=send_data)
    task.run()

run_thread()
