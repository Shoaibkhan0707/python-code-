def sortdecorator(fn):
        def bubble(l):
                for i in range(1,len(l)):
                        for j in range(1,len(l)-i+1):
                                if l[i]<l[j-1]:
                                        l[j],l[j-1]=l[j-1],l[j]
                fn(l)
        return bubble

@sortdecorator
def listprinter(l):
	for i in range(len(l)):
		print(l[i],end=' ')
	print()
l=[1,5,2,8,9,3,7]
listprinter(l)
