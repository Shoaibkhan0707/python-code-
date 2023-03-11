l=[3,5,7,2,4,6]
length=len(l)
i=1
while(i<length):
    j=i;min=i-1
    while(j<length):
            if l[j]<l[min]:
                min=j
            j=j+1
    l[i-1],l[min]=l[min],l[i-1]
    i=i+1
print(l)
