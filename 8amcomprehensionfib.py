def fib(x):
	if x==1 or x==2:
		return 1
	return fib(x-2)+fib(x-1)
l=[fib(x) for x in range(1,11)]
print(l)
