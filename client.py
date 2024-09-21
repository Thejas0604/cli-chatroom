import socket, threading

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(("127.0.0.1", 3002))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode("ascii")
            if msg == "NICKNAME":
                client.send(nickname.encode("ascii"))
            else:
                print(msg)
        except:
            print("Error occured!!!!")
            client.close()
            break
        
def write():
    while True:                                             
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)              
receive_thread.start()
write_thread = threading.Thread(target=write)                  
write_thread.start()