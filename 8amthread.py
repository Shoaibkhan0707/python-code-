from threading import *
def printer(x):
	for i in range(x,5000):
		print(i)
t1=Thread(target=printer,args=(10,))
t2=Thread(target=printer,args=(15,))
t1.start()
t2.start()
