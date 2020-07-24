import socket

# socketObj = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socketObj = socket.socket()
socketObj.bind(('',12333))

socketObj.listen()

try:
    while True:
        clientSocket,client_RetAddress =socketObj.accept()
        print("Request from ",clientSocket,client_RetAddress)
        received = clientSocket.recv(1024)
        print (received.decode())
        clientSocket.send(b"Hi from the server!")
        clientSocket.close()

except Exception as e:
    print("Something terrible happened. Run for your life!! Server shutting down!!")
    print(e)
    socketObj.close()