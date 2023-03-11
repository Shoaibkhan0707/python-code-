class myclass(object):
	def __init__(self):
		self.x=10
	def printer(self):
		print(self.x)
m=myclass()
m.printer()
print(dir(m))
o=object()
print(dir(o))
