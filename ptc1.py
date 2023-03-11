def search(ar,low,high,data):
	if(low<=high):
		mid=low+high//2
		if(ar[mid]==data):
			return mid
		elif(ar[mid]<data):
			return search(ar,mid+1,high,data)
		else:
			return search(ar,low,mid-1,data)
	return -1
l=[1,8,7,6,5,4,3,2];
length=len(l)
find=30;
result=search(l,0,length-1,find)
if(result!=-1):
	print("data found")
else:
	print("data not found")

