fd=None
filename=input("enter file name to be opened__")
try:
	fd=open(filename,'r')
	for line in fd:
		print(line,end='')
	print()
except:
        print('file does not be opened re enter filename')
	filename=input()
	try:
		fd=open('filename'.'r')
		for line in fd:
			print(line,end='')
		print()
	except:
		print('again file does not exit,terminating process')
		exit()
	finally:
		if fd!=None:
		fd.close()

