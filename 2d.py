l=[2,3,5]
l2=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(l2[1][2])
print(l2)
i=0
while i<len(l2):
	j=0
	while j<len(l2[i]):
		print(l2[i][j],end='')
		j+=1
	print('\n')
	i+=1
