def search(fn):
	def binarysearch(l,si,li,e,k):
		while si<li:
			mid=(si+li)//2
			if l[mid]==e:
				k=mid
				return
			elif l[mid]>e:
				li=mid-1
			else:
				si=mid+1
		k=-1
		fn(l,si,li,e,k)
	return binarysearch

def sort(fn):
	def bubblesort(l,si,li,e,k):
		for i in range(1,len(l)):
			for j in range(1,len(l)-i+1):
				if l[j]<l[j-1]:
				 	l[j],l[j-1]=l[j-1],l[j]
		fn(l,si,li,e,k)
	return bubblesort

@sort
@search
def printelement(l,si,li,e,k=-1):
	if k!=-1:
		print('element found',k)
	else:
		print('element not found')
l=[5,8,3,2,1,7,6]
printelement(l,0,len(l)-1,4,-1)
