def sortdecorator(fn,l):
	def bubble():
		for i inr range(1,len(l)):
			for j in range(1,len(l)-i+1):
				if l[i]<l[j-1]:
					l[j],l[j-1]=l[j-1],l[j]
		fn(l)
	return bubble
