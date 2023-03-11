import MySQLdb
import os
def toclear():
	os.system('clear')
	print('welcome to search staff')
def welcome():
	name=input('enter staff name:')
	return name
def searchstaff(name):
	con=MySQLdb.connect(host='localhost',database='visitordb',user='shoaib',password='admin@123')
	cur=con.cursor()
	t=(name)
	str="select * from staff_table where(staff_name='%s')"
	cur.execute(str%t)
	data=cur.fetchall()
	return data

def staffexists(data):
	choice=int(input('option\n 1.father_name\n 2.staff_mob_no\n 3.exit\n'))
	toclear()
	if choice==1:
		flag=0
		x=input('enter the father name :\n')
		for d in data:
			for i in d:
				if x==i:
					print('datafound')
					insert(data)
					display(data)
					exit()
					flag=1
			break
		if flag==0:
			os.system('clear')
			print('not found')
			staffexists()
	elif choice==2:
		flag=0
		y=input('enter the staff_mobile_no :\n')
		for d in data:
			for i in d:
				if y==i:
					print('data found')
					insert(data)
					display(data)
					exit(data)
					flag=1
			break
		if flag==0:
			os.system('clear')
			print('data not found')
			staffexists(data)
	else:
		exit()
		os.system('clear')
def getid():
	con=MySQLdb.connect(host='localhost',database='visitordb',user='shoaib',password='admin@123')
	cur=con.cursor()
	os.system('clear')
	str="SELECT visitor_id from log_table order by visitor_id  desc limit 1"
	data=cur.execute(str)
	data=cur.fetchall()
	id=data[0]
	x=id[0]
	return x

def insert(data):
	con=MySQLdb.connect(host='localhost',database='visitordb',user='shoaib',password='admin@123')
	cur=con.cursor()
	os.system('clear')
	final=[]
	id1=getid()
	final.append(id1+1)
	x=input('enter the visitor_name\n')
	final.append(x)	
	sid=data[0]
	sfid=sid[0]
	final.append(sfid)
	y=input('enter the purpose\n')
	final.append(y)
	z=input('enter the phone_number\n')
	final.append(z)
	t=tuple(final)
	query="insert into log_table(visitor_id,visitor_name,staff_id,time,purpose,status,visitor_phone)values('%d','%s','%d',NOW(),'%s','0','%s')"
	cur.execute(query%t)
	con.commit()
	cur.close()
	con.close()


def display(data):
	os.system('clear')
	con=MySQLdb.connect(host='localhost',database='visitordb',user='shoaib',password='admin@123')
	cur=con.cursor()
	#os.system('clear')
	id1=data[0]
	sfid=id1[0]
	print('staff is located at')
	str="select building_name,floor_no,room_no from staff_location where(staff_id='%d')"
	data=cur.execute(str%sfid)
	data=cur.fetchall()
	data1=data[0]
	building=data1[0]
	floor=data1[1]
	room=data1[2]
#	print('building_no',end=' ')
	print(building)
#	print('floor_no',end=' ')
	print(floor)
#	print('room',end=' ')
	print(room)

def exit():
	os.system('clear')
	con=MySQLdb.connect(host='localhost',database='visitordb',user='shoaib',password='admin@123')
	cur=con.cursor()
	n=int(input('please show your visitor_id\n'))
	id=(n)
	str="update log_table set status=1,exit_visitor=NOW() where(visitor_id='%d')"
	data=cur.execute(str%id)
	con.commit()
	cur.close()
	con.close()
	print('\n')

