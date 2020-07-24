import socket

socketObj = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socketObj.bind(('localhost', 12345))
print (socketObj)
try:
    socketObj.sendto(b"Hello from socket 1!",('localhost', 12344))
    received = socketObj.recv(1024)
    print(received)
except Exception as e:
    print ("Exception occured")
    print (e)
    socketObj.close()
