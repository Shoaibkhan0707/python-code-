def bubble(a,n):
#length=len(l)
    if n==1:
        return n
    for i in range(n):
        for j in range(i+1):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
    bubble(a,n-1)
l=[8,7,9,6,4,3,2,1]
length=len(l)
bubble(l,length)
print(l)
