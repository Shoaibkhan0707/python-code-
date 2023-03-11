import os.path
if  os.path.isfile('sample.txt'):
	fp=open('sample.txt','rb')
	fp.seek(10,0)
	for line in fp:
		print(line,end='')
	print()
	#fp.close()
else:
	print('file does not exit')
