def ex(a,b):
    try:
        return a/b
    except:
        return("divided by zero")
a=ex(10,2)
print(a)
b=ex(2,0)
print(b)
