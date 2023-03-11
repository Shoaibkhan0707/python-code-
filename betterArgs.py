def printer(*args,**kwargs):
	for i in args:
		print(i,end=' ')
	print('\n')
	for j in kwargs.keys():
		print(kwargs[j],end=' ')
	print('\n')
printer(2,3,5,age=20,salary=5000)
