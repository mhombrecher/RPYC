import rpycprotocol

class RPyCProxy:
	def call(self, func_name, *args, **kwargs):
		request = funcName2String(func_name, args, kwargs)
		
		
	def addHandler(self, han):
		self.handler = han
		
		
		