import copy
l=[1,2,3]
l2=copy.deepcopy(l)
print(l is l2)
l3=[1,[2,3],4]
l4=copy.deepcopy(l3)
print(l3 is l4)
l[1]=5
print(l)
print(l2)
l3[1][0]=10
l3.append(15)
print(l3)
print(l4)
