fd=None
filename=input("enter file name to be opened__")
try:
	fd=open(filename,'r')
except:
	print('file can not be opened')
	exit()
for line in fd:
	print(line,end='')
print()
fd.close()
