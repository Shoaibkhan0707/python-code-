def maxnum (x):
    return sum(x)-min(x)
def minnum(x):
    return sum(x)-max(x)
a = list(range(6))
print(a)
print(maxnum(a),minnum(a))
