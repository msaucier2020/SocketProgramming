from socket import *

serverIP = '127.0.0.1'
serverPort = 8001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))

client_int = int(input("Enter an integer 1 to 100: "))
client_name= "Client of Madeleine Saucier"
client_message = client_name + " " + str(client_int)

clientSocket.send(client_message.encode())
serv_message = clientSocket.recv(5010).decode()

serv_name = ''.join([i for i in serv_message if not i.isdigit()])

for x in serv_message.split():
    if(x.isdigit()):
        serv_int = int(x)

sum = serv_int + client_int

print(client_name)
print(serv_name)
print("Client int: " + str(client_int))
print("Server int: " + str(serv_int))
print("Sum: " + str(sum))


clientSocket.close()
