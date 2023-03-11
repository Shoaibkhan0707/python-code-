l=[3,2,5,7,4,18,19,9,8]
print(l)
length=len(l)
i=1;
while(i<length):
    temp=l[i]
    j=i
    while j>=0 and temp<=l[j]:
        if temp<l[j]:
         	l[j+1]=l[j]
        j=j-1
    l[j+1]=temp
    i=i+1;
print(l)    
