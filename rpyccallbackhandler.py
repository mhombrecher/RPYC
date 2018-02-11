import json

class RPyCCallbackHandler:
	
	functionBindings = {}
	
	def addCallback(self, func):
		if callable(func):
			self.functionBindings[func.__name__] = func
#			print("RPC added: ", self.functionBindings)
			
	def call(self, func_name, *args, **kwargs):
		func = self.functionBindings[func_name]
		if func: 
			return (func(*args, **kwargs))
		else: return None	
	
	def callRequest(self, requestString):
		print("RPyCCallbackHandler:callRequest: ".format(requestString))
		paras = json.loads(requestString)
		name = paras["func"]
		args= paras["args"]
		kwargs = paras["kwargs"]
		return self.call(name, *args, **kwargs )

		
