class student:
	def __init__(self,age,gender):
		self.age=age
		self.gender=gender
	class name:
		def __init__(self,fn,mn,ln):
			self.firstname=fn
			self.lastname=ln
			self.middlename=mn
		def nameprinter(self):
			print('{} {} {}'.format(self.firstname,self.lastname,self.middlename))
	def printer(self):
		print('age is {} and gender is'.format(self.age,self.gender))
s=student(30,'male').name('amit','kumar','verma')
s.nameprinter()
s.printer()
#n=s.name('amit','kumar','verma')
#n.nameprinter()
#print(type(n))

