l=[1,2,3,4,5,6,8,12,15]
i=0;j=len(l)-1
mid=0
se=8
check=0
while i<=j:
    mid=(i+j)//2
    if l[mid]==se:
        print("found",i)
        check=1
        break
    elif l[mid]<se:
        i=mid+1
    else:
        j=mid-1
if check==0:
        print("not found")
