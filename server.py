import socket

#####################
serverip = '192.168.0.100'
port = 9000
#####################

buffsize = 4096

while True:
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.bind((serverip,port))
	server.listen(1)
	print('waiting micropython...')

	client, addr = server.accept()
	print('connected from:', addr)

	data = client.recv(buffsize).decode('utf-8')
	print('Data from MicroPython: ',data)
	client.send('received your messages.'.encode('utf-8'))
	client.close()





