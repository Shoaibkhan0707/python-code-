import pickle
class student:
	def __init__(self,name,age,college):
		self.name=name
		self.age=age
		self.college=college
	def printer(self):
		print('{ },{ },{ }'.format(self.name,self.age,self.college))
s1=student('mukesh',20,'bbd')
s2=student('nahesh',21,'integral')
s3=student('suresh',20,'integral')
fp=open('sample.dump','wb')
pickle.dump(s1,fp)
pickle.dump(s2,fp)
pickle.dump(s3,fp)
while true:
	stu=pickle.load('sample.dump')
	stu.printer()
pickle.close()
