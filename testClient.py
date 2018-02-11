import socket
import sys
from rpycprotocol import funcName2Buffer, buffer2Value


HOST, PORT = "localhost", 9999

data = funcName2Buffer('testFunc', *sys.argv[1:])
data = funcName2Buffer('testFunc', "Hallo", 'Echo', eins='zwöi', zwei=1345, drei='Brötßpinne')


# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	# Connect to server and send data
	sock.connect((HOST, PORT))
	sock.sendall(bytes(data))

	# Receive data from the server and shut down
	received = sock.recv(1024)
	result = buffer2Value(received)
finally:
	sock.close()

print("Sent:     {}".format(data))
print("Received: {}".format(result))
