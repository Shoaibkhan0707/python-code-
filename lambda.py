def dtime(fn,data,term):
    a=1
    for i in range(1,term+1):
        a*=fn(data)
    return a
x=dtime(lambda x:x*10,2,5)
print(x)
