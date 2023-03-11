def three(a=0,b=0,c=0):
    print(a,b,c)
    def max(x,y):
        if x>=y:
            return x
        else:
            return y
    t=max(a,b)
    s=max(t,c)
    return s
x=three(2)
y=three(b=2,c=5,a=8)
print(x,y)
