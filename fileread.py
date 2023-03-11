filename="abc.text"
with open(filename,'r') as ff:
	data=ff.read()
	#print(data)
	print(data.rstrip())
#for line in data:
#	print(line)


