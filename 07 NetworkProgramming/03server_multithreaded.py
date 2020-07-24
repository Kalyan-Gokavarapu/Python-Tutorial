import socket
import threading

class processRequest(threading.Thread):
    def __init__(self, socket):
        # super processRequest, self).__init__()
        # can use the above as well to call the base class constructor
        threading.Thread.__init__(self)
        self.socket = socket
       
        
    def run(self):
        clientSocket = self.socket
        clientSocket.send(b"Roger that!")
        received = clientSocket.recv(1024)
        print (received.decode())        
        clientSocket.close()

# socketObj = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socketObj = socket.socket()
socketObj.bind(('',12333))
socketObj.listen()
print('Server is ready! listening for request on port: 12333')

try:
    while True:
        clientSocket,client_RetAddress =socketObj.accept()
        print("Request from ",clientSocket,client_RetAddress)
        procThread = processRequest(clientSocket)
        procThread.start()  

except Exception as e:
    print("Something terrible happened. Run for your life!! Server shutting down!!")
    print(e)
    socketObj.close()
