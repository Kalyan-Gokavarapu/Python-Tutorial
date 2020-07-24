import socket

socketObj = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socketObj.bind(('localhost', 12344))
print (socketObj)
try:
    received = socketObj.recv(1024)
    socketObj.sendto(b"Hello there from socket 2!",('localhost', 12345))    
    print(received)
except Exception as e:
    print ("Exception occured")
    print (e)
    socketObj.close()
