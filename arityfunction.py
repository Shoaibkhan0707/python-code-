def sum(x,y,*z):
    t=x+y
    for i in z:
        t+=i
    return t
s=sum(2,3,5,8)
print(s)
t=sum(5,8)
print(t)
