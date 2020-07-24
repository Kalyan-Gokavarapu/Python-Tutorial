import socket

socketObj = socket.socket()
socketObj.connect(('localhost',12333))
socketObj.send(b'Hi from Client1!')

socketObj = socket.socket()
socketObj.connect(('localhost',12333))
socketObj.send(b'Hi from Client2!')

socketObj = socket.socket()
socketObj.connect(('localhost',12333))
socketObj.send(b'Hi from Client3!')

socketObj = socket.socket()
socketObj.connect(('localhost',12333))
socketObj.send(b'Hi from Client4!')

received = socketObj.recv(1024)
print(received.decode())
socketObj.close()
