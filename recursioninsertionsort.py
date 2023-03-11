def insertion(a,n):
    if n==1:
        return n
    for i in range(1,n):
        temp=a[i]
        j=i-1
        while j>=0 and temp<=a[j]:
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp
    insertion(a,n-1)
l=[8,7,9,6,4,3,2,1]
length=len(l)
insertion(l,length)
print(l)
