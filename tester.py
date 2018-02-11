from rpycprotocol import funcName2Buffer, buffer2Request, value2Buffer, buffer2Value
from rpyccallbackhandler import RPyCCallbackHandler as CallbackHandler
from rpycproxy import RPyCProxy as Proxy



#testmessage = testmessage = 'Hallo, liebe Läute ... wie geht eß denn sö? !"§$ - '
#byte_buffer = rpycprotocol.encode(testmessage)
#the_string = rpycprotocol.decode(byte_buffer)
#print (the_string)


myHandler = CallbackHandler()

def testFunc(*args, **kwargs):
	myresult = []
	myresult.append("hallo Testfunktion!")
	for value in args:
		myresult.append(value)
		
	for key, value in kwargs.items():
		myresult.append(key + ": " + str(value).upper() )

	return myresult
#	return 9

	
	

myHandler.addCallback(testFunc)

#myProxy = Proxy()
#myProxy.addHandler(myHandler)
#request = Proxy.call('testFunc', 20,30,40,90, hans = "Im Füchßloch 9", Mötörhead=8, Frau="Simone-Heinz")

#print ("Ergebnis = {}".format(request))
#result = myHandler.callRequest(request)
#result = myHandler.call('testFunc', 16, 9, 'werner' , Name='hans', Alter=64)
#print (result)

#Client
print ('calling testFunc(20,30,40,90, hans = "Im Füchßloch 9", Mötörhead=8, Frau="Simone-Heinz")')
myBuf = funcName2Buffer('testFunc', 20,30,40,90, hans = "Im Füchßloch 9", Mötörhead=8, Frau="Simone-Heinz")
# Hier muß erfolgen: Übertragung mybuf von Client an Server 

#Server
request = buffer2Request(myBuf) #Request (UTF-8 String im JSON Format) Auspacken
result =  myHandler.callRequest(request) # Ausführen
myBuf = value2Buffer(result) #Ergebnis einpacken (UTF-8 String im JSON Format

# Hier muss erfolgen: Übertragung von myBuf an Client
#Client
result = buffer2Value(myBuf)

	
print (result)
	

	
	