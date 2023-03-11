def max(a,b,c):
    def three(x,y):
        if x>=y:
            return x
        else:
            return y
    t=three(a,b)
    s=three(t,c)
    return s
x=max(10,20,15)
print(x)
    
