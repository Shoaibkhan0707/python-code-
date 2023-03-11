from tkinter import *
import MySQLdb
class loginform:
	def __init__(self,root):
		self.f=Frame(root,height=500,width=500)
		self.f.propagate(0)
		self.f.pack()
		self.heading=Label(text='REGISTRATION FORM',font=('arial',20,'bold'),fg='red')
		self.uname=Label(text='Enter Email:',font=('arial',15,'bold'))
		self.password=Label(text='Enter password:',font=('arial',15,'bold'))
		self.fname=Label(text='First Name:',font=('arial',15,'bold'))
		self.lname=Label(text='Last Name:',font=('arial',15,'bold'))
		self.db=Label(text='D.O.B:',font=('arial',15,'bold'))
		self.day=Label(text='day',font=('arial',15,'bold'))
		self.month=Label(text='month',font=('arial',15,'bold'))
		self.year=Label(text='year',font=('arial',15,'bold'))
		self.gender=Label(text='gender:',font=('arial',15,'bold'))
		self.male=Label(text='male',font=('arial',15,'bold'))
		self.female=Label(text='female',font=('arial',15,'bold'))

		self.e1=Entry(self.f,width=25,fg='blue',bg='white')
		self.e2=Entry(self.f,width=25,fg='blue',bg='white',show='*')
		self.e3=Entry(self.f,width=25,fg='blue',bg='white')
		self.e4=Entry(self.f,width=25,fg='blue',bg='white')
		self.e5=Entry(self.f)
		self.db1=Entry(self.f,width=25,fg='blue',bg='white')
		self.day1=Label(self.f,width=25)
		self.month1=Label(self.f,width=25)
		self.year1=Label(self.f,width=25)
		self.gender1=Label(self.f,width=25)
		self.male1=Label(self.f,width=25)
		self.female1=Label(self.f,width=25)

		self.b=Button(self.f,text='submit',font=('arial',15,'bold'),fg='blue',height=2,width=15,command=lambda:self.datagetter())
		self.b.place(x=100,y=400)

		self.uname.place(x=50,y=100)
		self.e1.place(x=100,y=100)

		self.password.place(x=50,y=150)
		self.e2.place(x=100,y=150)

		self.fname.place(x=50,y=200)
		self.e3.place(x=100,y=200)

		self.lname.place(x=50,y=250)
		self.e4.place(x=100,y=250)

		self.heading.place(x=800,y=10)
		self.e5.place(x=100,y=100)

		self.db.place(x=50,y=300)
		self.db1.place(x=100,y=20)

		self.day.place(x=150,y=300)
		self.day1.place(x=100,y=10)

		self.month.place(x=220,y=300)
		self.month1.place(x=100,y=10)

		self.year.place(x=320,y=300)
		self.year1.place(x=100,y=10)

		self.gender.place(x=50,y=350)
		self.gender1.place(x=100,y=350)

		self.male.place(x=180,y=350)
		self.male1.place(x=100,y=15)

		self.female.place(x=300,y=350)
		self.female1.place(x=100,y=10)

		self.s1=Spinbox(self.f,from_=1,to=31,textvariable=self.day,width=6,fg='black',bg='white',font=('Arial',10,'bold'))

	def datagetter(self):
		con=MySQLdb.connect(host='localhost',database='welcome',user='shoaib',password='admin@123')
		cur=con.cursor()
		l=[]
		str="insert into user_info(email,password)values('%s','%s')"
		ustr=self.e1.get()
		pstr=self.e2.get()
		ab=self.e3.get()
		cd=self.e4.get()
		l.append(ustr)
		l.append(pstr)
		l.append(ab)
		l.append(cd)
		t=tuple(l)
		cur.execute(str%t)
		con.commit()
		cur.close()
		con.close()
		print('username:',ustr)
		print('password:',pstr)
		print('firstname',ab)
		print('lastname',cd)
root=Tk()
fo=loginform(root)
root.mainloop()

