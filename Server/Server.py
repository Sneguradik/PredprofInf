import asyncio, threading, socket

HOST = '127.0.0.1'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
print("Run")

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
            threading.Thread.__init__(self)
            self.csocket = clientsocket
    def run(self):
        msg = ''
        while True:
            data =  self.csocket.recv(4096)
            msg = data.decode()
            if msg == '':
                break

while True:
    server.listen(1)
    clientsock, clientAddress =server.accept()
    newthread = ClientThread(clientAddress, clientsock)
