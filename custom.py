import copy
class copydemo:
	def __init__(self):
		self.x=10
		self.y=20
		self.l=[1,2,3]
	def printer(self):
		print(self.x)
		print(self.y)
		print(self.l)
cd=copydemo()
cd2=copy.deepcopy(cd)
cd.x=15
cd.l[1]=7
cd.printer()
cd2.printer()

