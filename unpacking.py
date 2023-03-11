def add(**kw):
	sum=0
	for item in kw.keys():
		sum+=kw[item]
	return sum
dict={'ramesh':1000,'suresh':2000,'magnesh':1500}
#print(a)
#l=(5,10,15,20)
b=add(**dict)
print(b)
