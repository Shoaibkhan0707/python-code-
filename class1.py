class myclass:
	def __init__(self):
		self.x=10
		self.name='sarla'
	def display(self):
		print(self.x)
		print(self.name)

m1=myclass()
m1.display()

m2=myclass()
m2.display()

m1.x=20
m1.display()

m2.display()
