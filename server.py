# socket for connect two nodes in a network
# threading for spawn multiple threads in a program.
import socket, threading 

host = "127.0.0.1"
port = 3002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# AF_INET: usage of internet sockets 
# SOCK_STREAM: usage of TCP
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# Broadcast msg
def broadcast(msg):
    for client in clients:
        client.send(msg)
        
def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(index)
            client.close()
            nickname = nicknames(index)
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def recieve():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))       
        client.send('NICKNAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start() 

recieve()