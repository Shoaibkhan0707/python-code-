import os.path
l=['/home/shoaib/abc.txt','/home','/','.','']
for p in l:
	print(os.path.split(p))
print(os.path.basename(l[0]))
print(os.path.dirname(l[0]))
print(os.path.splitext(l[0]))
