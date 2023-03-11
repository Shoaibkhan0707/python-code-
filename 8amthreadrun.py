from threading import *
class mythread(Thread):
	y=10
	def __init__(self,x):
		super().__init__()
		self.x=x
	def run(self):
		for i in range(mythread.y,5000):
			if mythread.y==10:
				mythread.y=self.x
			print(i)
t1=mythread(25)
t2=mythread(20)
t1.start()
t2.start()
