import MySQLdb
def welcome():
        print('welcome to staff search !')
        name=input('enter staff name:\n')
        return name
def searchstaff(name):
	con=MySQLdb.connect(host='localhost',database='visitordb',user='shoaib',password='admin@123')
	cur=con.cursor()
	t=(name)
	str="select * from staff_table where(staff_name='%s')"
	cur.execute(str%t)
	data=cur.fetchall()
	return data
def welcome2():
	choice=int(input("choose the option 1 and 2"))
	print('1.enter the father name\n')
	print('2.enter mobie number:\n')
#	choice=int(input("enter the option\n"))
	if choice==1:
		name1=input("enter the father name\n")
	return name1
	if choice==2:
		return name1
	if choice==2:
		name2=input("enter mobile number\n")
	return name2
def searchfather(name1):
	con=MySQLdb.connect(host='localhost',database='visitordb',user='shoaib',password='admin@123')
	cur=con.cursor()
	t1=(name1)
	str1="select * from staff_table where(staff_father_name='%s')"
	cur.execute(str1%t1)
	data1=cur.fetchall()
	return data1
def welcome3():
#        print('enter the option')
        name2=input('enter phone number:')
        return name2
def searchmob(name2):
        con=MySQLdb.connect(host='localhost',database='visitordb',user='shoaib',password='admin@123')
        cur=con.cursor()
        t2=(name2)
        str2="select * from staff_table where(staff_phone_no='%s')"
        cur.execute(str2%t2)
        data2=cur.fetchall()
        return data2
"""def call():
	while(1):
		option=(int(input("option\n 1.staff_name\n 2.searchfather_name\n 3.search_staff_mob_no\n 4.exit\n")))
		if option==1:
			searchstaff()
		if option==2:
			searchfather()
		if option==3:
			searchmob()
		if option==4:
			return 0
		if option>4:
			print("invalid option")

call()"""

