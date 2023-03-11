from screen import *
import MySQLdb
while True:
	choice=int(input(' 1.new_visitor\n 2.exit_visitor\n'))
	if choice==1:
		toclear()
		name=welcome()
		data=searchstaff(name)
		while len(data)==0:
			toclear()
			print('staff not found')
			name=welcome()
			data=searchstaff(name)
		toclear()
		staffexists(data)
	elif choice==2:
		exit()
		print('mission completed')
	else:
		exit()
#insert(data)
#for i in data:
#	print(i)
#insert()
#getdata(data)
"""name=welcome()
data=searchstaff(name)
while len(data)==0:
        toclear()
        print('staff not found')
        name=welcome()
        data=searchstaff(name)
toclear()
#staffexists(data)
#for i in data:
#	print(i)"""
"""while len(res)==0:
	for d in data:
		print(d)"""
"""if len(data)==0:
	toclear()
	print('no match found')
	name=welcome()
	data1=searchstaff(name)
	if len(data1)==0:
		toclear()
		print('not found')
	else:
		print('found data',data1)
#	print(searchstaff(x))
else:
	for d in data:
		print(d)"""
