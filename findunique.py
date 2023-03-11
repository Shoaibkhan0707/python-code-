def findunique(l):
	t=l[0]
	for i in range(1,len(l)):
		t=t^l[i]
	return t
l=[2,3,8,9,10,2,8,9,3]
print(findunique(l))
