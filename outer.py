x=15
def outer():
	global x
	x=10
	print(x)
	def inner():
		global x
		x+=2
		print(x)
	inner()
	print(x)
outer()
