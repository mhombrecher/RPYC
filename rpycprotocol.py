import hashlib
import json

	
version = 'rpc01.00'
	
def rpycencode(dstring):
	"""	expects a String of arbitraty length returns a buffer byte buffer 
	- (8 Bytes) begins with encoded Versionstring is 8 Bytes "rpcXX.XX" where X are numbers (e.g. rpc01.00)
	- (8 Bytes) continues with overal meesage lenght in Bytes- an Integer represented as 8 Bytes in 'little' encoding
	- (32 Bytes) continues with a SHA-265 hash key of the UTF-8 encoded dstring
	- (arbitrary) continues with the payload (dstring encoded in UTF-8) 
	"""
	
	rpcversion = version.encode()
	pay_load = dstring.encode()
	hs = hashlib.sha256()
	hs.update(pay_load)
	hash_key = hs.digest()
	
#	print ("Hashkey = {0}, Länge = {1}".format(hs.hexdigest(), len(hash_key)))
	b_length = len (rpcversion) + 8 + len(hash_key) + len(pay_load)
	resultBytes = rpcversion + b_length.to_bytes(8, byteorder = 'big') + hash_key + pay_load
	return resultBytes

def rpycdecode(dbuffer):
	"""	expects a byte buffer of arbitrary length but encoded with the below listed protocol. Returns the payload as a UTF-8 String
	- (8 Bytes) begins with encoded Versionstring is 8 Bytes "rpcXX.XX" where X are numbers (e.g. rpc01.00)
	- (8 Bytes) continues with overal meesage lenght in Bytes- an Integer represented as 8 Bytes in 'little' encoding
	- (32 Bytes) continues with a SHA-265 hash key of the UTF-8 encoded dstring
	- (arbitrary) continues with the payload (dstring encoded) 
	returns a  Unicode String as a result
	"""
	payload = ''
	rpcversion = version.encode()
	bprot = dbuffer[0:8]
	if rpcversion != bprot: print("Error wrong protocol version {}".format(bprot))
	else: 
		blength = dbuffer[8:16]
		bHash = dbuffer[16:48]
		bPayload = dbuffer[48:]
		length = int.from_bytes(blength, byteorder='big')
		prot = bprot.decode() # This is the Python decode method for bytes to Unicode String decoding
		payload = bPayload.decode() # This is the Python decode method for bytes to Unicode String decoding
#		print ("Protocol: {0}, Length: {1}, Hash: {2}".format(prot, length, bHash.hex()))
		
	return payload
	

#	def func2String(func, *args, **kwargs):
#		myargs = {'func': func.__name__, 'args': args, 'kwargs': kwargs}
#		result = json.dumps(myargs, ensure_ascii=False, separators=(',', ':'))
#		return result

def funcName2String(funcName, *args, **kwargs):
	myargs = {'func': funcName, 'args': args, 'kwargs': kwargs}
	result = json.dumps(myargs, ensure_ascii=False, separators=(',', ':'))
	return result

def funcName2Buffer(funcName, *args, **kwargs):
	return rpycencode(funcName2String(funcName, *args, **kwargs))
	
def buffer2Request(dbuffer):
	return rpycdecode(dbuffer)
	
def value2Buffer(myVar):
	""" Takes any Python variable as input, converts in to a json string and subsequetly returns a rpyc buffer ready for transmission"""
	resultString = json.dumps(myVar, ensure_ascii=False, separators=(',', ':')) 
	return rpycencode(resultString)
	
def buffer2Value(mybuf):
	""" Takes a rpyc buffer containing a json format and unpacks  and returns the contained value """
	jString = rpycdecode(mybuf)
	return json.loads(jString)
	
		
		
		
		
		
		
		


