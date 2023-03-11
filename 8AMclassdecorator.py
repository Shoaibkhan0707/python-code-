def singleton(cls):
	instance=None
	def get_instance(x):
		nonlocal instance
		if instance is None:
			intance=cls(x)
		return instance
	return get_instance
@singleton
class myclass(object):
	def __init__(self,x):
		self.x=x
	def printer(self):
		print(self.x)

m1=myclass(10)
m2=myclass(20)
m1.printer()
m2.printer()
