from socket import *

serverIP = '127.0.0.1'
serverPort = 8001

#connect client to server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))

#accept input for integer and create client message
client_int = int(input("Enter an integer 1 to 100: "))
client_name= "Client of Madeleine Saucier"
client_message = client_name + " " + str(client_int)

#send encoded message to server
clientSocket.send(client_message.encode())
print("Message sent to server")

#receive and decode message from server
serv_message = clientSocket.recv(5010).decode()
print("Server message received")

#get just server name from message
serv_name = ''.join([i for i in serv_message if not i.isdigit()])

#get integer from server message
for x in serv_message.split():
    if(x.isdigit()):
        serv_int = int(x)

#compute sum
sum = serv_int + client_int

#print all info
print(client_name)
print(serv_name)
print("Client int: " + str(client_int))
print("Server int: " + str(serv_int))
print("Sum: " + str(sum))


clientSocket.close()
print("Client socket closed")