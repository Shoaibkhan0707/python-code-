filename1='copywrite.text'
with open(filename1,'r')as frd:
        data=frd.read()
count=0
for i in data:
	if data[i]=="32":
		count=count+1
	if i>0:
		count=count+1
	print(count)

