class myclass:
	x=10
	def __init__(self):
#		self.x=10
		self.name='arpit'
	@classmethod
	def myclassmethod(cls):
		m1=myclass()
		print(cls.x)
#		pass
	def myobjectmethod(self):
			print(myclass.x)
			print(self.name)
#myclass.myclassmethod()
m=myclass()
print(myclass.x)
m.x=15
myclass.myclassmethod()
print(myclass.x)
#m.myobjectmethod()
