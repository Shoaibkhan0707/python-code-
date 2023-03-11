from threading import *
def show():
	for i in range(1,100):
		print('from show'+str(i))
#		print(current_thread().is_alive())
t=Thread(name='mythread',target=show)
t.start()
#t.join()
#t.run()
print(t.is_alive())
print(t.getName())
for i in range(10,500):
	print(i)
print(t.is_alive())
