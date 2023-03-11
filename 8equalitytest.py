class tester:
	def __init__(self):
		self.x=10
		self.y=20
	def printer(self):
		print('{}{}'.format(self.x,self.y))
	def __str__(self):
		return 'this is object of tester class'
	def __repr__(self):
		return 'this is object of tester'
t1=tester()
a=str(t1)
print(a)
b=repr(t1)
print(b)
#repr(t1)
#t2=t1
#t1.x=30
#print(t1==t2)
#print(t1 is t2)
#t1.printer()
#t2.printer()
