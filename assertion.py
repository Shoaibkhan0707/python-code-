def discount(price,disc):
	newprice=price*(1-(disc/100))
	assert 0<=newprice<=price,'newprice is invalid'
	return newprice
x=discount(5000,10)
print(x)
#y=discount(5000,110)
#print(y)
print(callable(x)) # check predefined function work kr rha hai ya nhi
print(callable(discount))
