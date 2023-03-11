def three(a,b,c):
    def max(x,y):
        if x>=y:
            return x
        else: #function->function ko return bhi kr sakta hai
            return y
    def min(x,y):
        if x<=y:
            return x
        else:
            return y
    if a>=b:
        return max
    else:
        return min
m=three(2,3,5)
print(m(5,7))
