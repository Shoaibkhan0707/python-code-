import re
fp=open('email.text','r')
s=fp.read()
x=re.findall('[a-zA-Z][a-zA-Z0-9]*@[a-zA-Z0-9]+.[a-zA-Z0-9]+',s)
print(x)
