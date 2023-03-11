a=[1,6,9,4,3,7,8,2]
b=[]
i=0
length=len(a)
j=length-1
a.sort()
if length%2==0:
    while i<j:
        b.append(a[j])
        b.append(a[i])
        i=i+1
        j=j-1
else:
    while i<j:
        b.append(a[j])
        b.append(a[i])
        i=i+1
        j=j-1
    b.append(a[j])
print(b)

