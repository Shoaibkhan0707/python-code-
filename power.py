def fib(x,n):
	if x<0 or n<0:
		return none
	if n==1:
		return x 
	if n==0: 
		return 1
	return x*fib(x,n-1)
x=fib(2,3)
if x==None:
	print("negative")
else:
	print(x)

