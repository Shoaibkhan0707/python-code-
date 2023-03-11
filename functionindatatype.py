def fact(x):
    if(x==0 or x==1):
        return 1
    return x*fact(x-1)
b=[fact,1,2,3,4,5]
map(fact,b)
print(b)
