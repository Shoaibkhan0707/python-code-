l=[3,5,7,2,4,6]
length=len(l)
i=1
while(i<length):
    j=1
    while(j<=length-1):
        if l[j]<l[j-1]:
                l[j],l[j-1]=l[j-1],l[j]
        j=j+1
    i=i+1;
print(l)

