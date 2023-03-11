#def fib(n):
#    if(n==1 or n==2): 
#        return 1
#    return fib(n-1)+fib(n-2)
#x=int(input("enter the number"))
#for i in range(1,10):
#	print(fib(i))

def fib(n):
	a=1;b=1;c=0
	if n==1 or n==2:
		return 1
	for i in range(3,n+1):
		c=a+b
		a=b
		b=c
	return c
#	print(a)
#fib(50)
term=int(input("enter the number:"))
for i in range(1,term+1):
	print(fib(i),end=' ')
print('\n')

