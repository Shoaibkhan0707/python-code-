class myclass(object):
	def __init__(self):
		self.x=10
	def mydecorator(fn):
		def decorated(self):
			print("hello")
			fn(self)
			print("bye")
		return decorated
	@mydecorator
	def myfn(self):
		print(self.x)
m=myclass()
m.myfn()
