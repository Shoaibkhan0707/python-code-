l=['a','b','c','a']
count=1
res=0
for i in range(len(l)):
	if l[i]==l[res]:
		count=count+1
	else:
		count=count-1
	if count==0:
		res=i
		count=1
print(l[res])
