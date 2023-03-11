class staticdemo:
	x=0
	def __init__(self):
		self.y=20
	def creator(self):
		self.x=30
s1=staticdemo()
s2=staticdemo()
print(staticdemo.x)
print(s1.x)
print(s2.x)
staticdemo.x=7
s1.x=7
print(s1.x)
print(s1.x)
print(s1.x)
s1.creator()
print(s1.x)
print(s1.__class__.x)
