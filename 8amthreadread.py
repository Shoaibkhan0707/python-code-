from threading import *
def filereader(s):
	f=open(s,'r')
	data=f.read()
	for line in data:
		print(line,end='')
	print()
t1=Thread(target=filereader,args=('sample.txt',))
t2=Thread(target=filereader,args=('abc.text',))
t1.start()
t2.start()
