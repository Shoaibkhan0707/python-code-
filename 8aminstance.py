class myclass:
	def __init__(self):
                self.x=10 #ek class mein ek he constructor bna sakte hain:
                self.name='mohan'
	def __init__(self,a):
		self.x=a
		self.name='suresh'
	def display(self):
        	print(self.x)
        	print(self.name)

m1=myclass(10)
m1.display()
#m2=myclass(20)
#m2.display()

#m1.x=20
#m1.display()

#m2.display()


