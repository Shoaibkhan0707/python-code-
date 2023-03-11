from demoscreen import *
import MySQLdb
name=welcome()
data=searchstaff(name)

name1=welcome2()
data1=searchfather(name1)

name2=welcome3()
data2=searchmob(name2)

if len(data)==0:
        print('no match found')
else:
        for d in data:
                print(d)
if len(data1)==0:
	print('no match found')
else:
	for i in data1:
		print(i)
if len(data2)==0:
	print('no match found')
else:
	for m in  data2:
		print(m)

