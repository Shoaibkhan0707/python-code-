def mydecorator(fn):
	def abc():
		print("decorating")
		fn()
		print('decorater')
	return abc # this is pythonic way:=
@mydecorator #using decorater 
def myfn():
	print('my function')
myfn()
#mydecorator(myfn)()
#a=mydecorator(myfn)
#a()
