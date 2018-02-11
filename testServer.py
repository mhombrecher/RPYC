import socketserver
from rpycprotocol import buffer2Request, value2Buffer
from rpyccallbackhandler import RPyCCallbackHandler as CallbackHandler




class MyTCPHandler(socketserver.BaseRequestHandler):
	"""
	The RequestHandler class for our server.

	It is instantiated once per connection to the server, and must
	override the handle() method to implement communication to the
	client.
	"""

	
	callbackHandler = CallbackHandler()
		
		
		
	def handle(self):
		# self.request is the TCP socket connected to the client
		self.data = self.request.recv(1024)
		request = buffer2Request(self.data) #Request (UTF-8 String im JSON Format) Auspacken
		result =  self.callbackHandler.callRequest(request) # Ausführen
		myBuf = value2Buffer(result) #Ergebnis einpacken (UTF-8 String im JSON Format

		print("{} wrote:".format(self.client_address[0]))
		print ("request = {}; result = {}".format(request, result))
		
		self.request.sendall(myBuf)

if __name__ == "__main__":
	HOST, PORT = "localhost", 9999

	# Create the server, binding to localhost on port 9999
	server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
	
	def testFunc(*args, **kwargs):
		myresult = []
		myresult.append("hallo Testfunktion!")
		for value in args:
			myresult.append(value)
			
		for key, value in kwargs.items():
			myresult.append(key + ": " + str(value).upper() )

		return myresult
		
		
	MyTCPHandler.callbackHandler.addCallback(testFunc)

	# Activate the server; this will keep running until you
	# interrupt the program with Ctrl-C
	server.serve_forever()