# skipping shebang for now

# from socket import *
import socket

serverPort = 12000 
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)	# create UDP socket
serverSocket.bind(('',serverPort))                      # bind socket to local port 12000
print "The server is ready to receive"

while 1:                                                # loop forever
  message, clientAddress = serverSocket.recvfrom(2048)  # read from UDP socket into message
  modifiedMessage = message.upper()                     # getting clients IP / port
  serverSocket.sendto(modifiedMessage,clientAddress)    # send upper case string back to client
						
