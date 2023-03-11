def max(a,b):
    if a>=b:
        return a
    else:
        return b
def three(a,b,c,fn):
    x=fn(a,b)
    y=fn(x,c)
    return y
t=three(5,7,3,max)
print(t)
