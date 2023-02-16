from socket import *
import random

serverIP = '127.0.0.1'
serverPort = 8001

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))

server_str = "Server of Madeleine Saucier"

serverSocket.listen(1) 
print("Server ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()

    client_message = connectionSocket.recv(5010).decode()
    client_name = ''.join([i for i in client_message if not i.isdigit()])
    for x in client_message.split():
        if(x.isdigit()):
            client_int = int(x)
    
    server_int = random.randint(0, 100)
    sum = server_int + client_int

    print(client_name)
    print(server_str)
    print("Client int: " + str(client_int))
    print("Server int: " + str(server_int))
    print("Sum: " + str(sum))

    server_message = server_str + " " + str(server_int)

    connectionSocket.send(server_message.encode())

    connectionSocket.close()