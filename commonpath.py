import os.path
l=['one/two/three','one/two/three/four','one/two/threefour']
print(os.path.commonprefix(l))
print(os.path.commonpath(l))
t=('/one','two','/three')
print(os.path.join(*t))
