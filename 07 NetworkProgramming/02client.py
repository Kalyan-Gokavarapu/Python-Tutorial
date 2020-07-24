import socket

socketObj = socket.socket()
socketObj.connect(('localhost',12333))
socketObj.send(b'Hi from Client!')

received = socketObj.recv(1024)
print(received.decode())
socketObj.close()
