def selection(a,n):
    mid=0
    if n==1:
        return n
    for i in range(n):
        mid=i
        for j in range(i+1):
            if a[mid]<a[j]:
                mid=j
                a[i],a[mid]=a[mid],a[i]
    selection(a,n-1)
l=[8,7,9,6,4,3,2,1]
length=len(l)
selection(l,length)
print(l)
