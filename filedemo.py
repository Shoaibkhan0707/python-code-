fd=open('sample1.txt')
fd2=open('sample2.txt','a')
for line in fd:
	if line.find('khan')!=-1:
		#with open(fd2,'w')as f1:
		fd2.write(line)
		#print(line.upper(),end="")
print()
fd.close()
fd2.close()

