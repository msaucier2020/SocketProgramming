from socket import *
import random

serverIP = '127.0.0.1'
serverPort = 8001

#create and bind socket to port
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))

server_str = "Server of Madeleine Saucier"

#open socket to receive messages
serverSocket.listen(1) 
print("Server ready to receive")


while True:
    connectionSocket, addr = serverSocket.accept()

    #receive and decode client message
    client_message = connectionSocket.recv(5010).decode()
    print("Client message received")

    #get client name from message
    client_name = ''.join([i for i in client_message if not i.isdigit()])

    #get integer from message
    for x in client_message.split():
        if(x.isdigit()):
            client_int = int(x)
    
    #get random integer and compute sum
    server_int = random.randint(0, 100)
    sum = server_int + client_int

    #print all info
    print(client_name)
    print(server_str)
    print("Client int: " + str(client_int))
    print("Server int: " + str(server_int))
    print("Sum: " + str(sum))

    #create server message, encode and send to client
    server_message = server_str + " " + str(server_int)
    connectionSocket.send(server_message.encode())
    print("Message sent to client")

    connectionSocket.close()
    print("Server socket closed")