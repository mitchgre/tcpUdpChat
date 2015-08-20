# skipping shebang for now... 

import sys
# the original import was:
# from socket import *
import socket


# serverName = 'hostname'
# get serverName from cl-args instead
serverName = sys.argv[1]
print serverName


serverPort = 12000
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message = raw_input('Input lowercase sentence:')
clientSocket.sendto(message,(serverName,serverPort))
# receive up to 2048 characters
modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
print "modified Message:"
print modifiedMessage
clientSocket.close()
