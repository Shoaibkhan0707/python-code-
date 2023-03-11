from threading import *
def show():
	for i in range(1,5000):
		print('from show:'+str(i))
def display():
	for i in range(1,5000):
		print('from display:'+str(i))
t=Thread(target=show)
t2=Thread(target=display)
t.start()
t2.start()
