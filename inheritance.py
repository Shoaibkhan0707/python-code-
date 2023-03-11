class parent(object):
	def __init__(self,a,b):
		self.x=a
		self.y=b
	def printer(self):
		print(self.x,self.y)
class child(parent):
	def __init__(self,t,s):
		super().__init__(t,s)
		self.z=30
	def printer(self):
		print(self.z)
		super().printer()
c=child(15,30)
c.printer()
print(type(c))
#print(c.z)
