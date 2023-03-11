from tkinter import *
import MySQLdb
class loginform:
	def __init__(self,root):
		self.f=Frame(root,height=500,width=500)
		self.f.propagate(0)
		self.f.pack()
		self.uname=Label(text='Enter email:')
		self.password=Label(text='Enter password:')
		self.e1=Entry(self.f,width=25,fg='blue',bg='white')
		self.e2=Entry(self.f,width=25,fg='blue',bg='white',show='*')
		self.b=Button(self.f,text='submit',height=2,width=10,command=lambda:self.datagetter())
		self.b.place(x=200,y=200)
		self.uname.place(x=50,y=100)
		self.e1.place(x=200,y=100)
		self.password.place(x=50,y=150)
		self.e2.place(x=200,y=150)
	def datagetter(self):
		con=MySQLdb.connect(host='localhost',database='loginform',user='shoaib',password='admin@123')
		cur=con.cursor()
		l=[]
		str="insert into form(email,password)values('%s','%s')"
		ustr=self.e1.get()
		pstr=self.e2.get()
		l.append(ustr)
		l.append(pstr)
		t=tuple(l)
		cur.execute(str%t)
		con.commit()
		cur.close()
		con.close()
		print('username:',ustr)
		print('password:',pstr)
root=Tk()
fo=loginform(root)
root.mainloop()
