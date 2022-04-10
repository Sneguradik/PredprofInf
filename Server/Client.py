import socket, threading

SERVER = '127.0.0.1'
PORT = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

def recivedata():
    while True:
        in_data = client.recv(4096)
        in_data = in_data.decode()
def senddata():
    while True:
        out_data = input()
        client.sendall(bytes(out_data, "UTF-8"))

t1 = threading.Thread(target=recivedata)
t2 = threading.Thread(target=senddata)

t1.start()
t2.start()