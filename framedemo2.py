from tkinter import *
class myclass:
	def __init__(self,root):
		self.f=Frame(root,height=400,width=500)
		self.f.propagate(0)
		self.f.pack()
		self.b=Button(self.f,text='red',width=15,height=2,command=lambda:self.buttonclicked(1))
		self.b.grid(row=1,column=1)
#		self.b.grid(row=0,column=0)
		self.b1=Button(self.f,text='olive',width=15,height=2,command=lambda:self.buttonclicked(2))
		self.b1.grid(row=2,column=1)
		self.c=Label(self.f,text='test',width=50,height=3,bg='green',fg='yellow')
		self.c.grid(row=0,column=1)
#		self.c.grid(row=2,column=3)
#		self.b1.pack(fill=X,padx=10,pady=10) # space  of lining
#		self.b.grid(row=0,column=1)
#		self.b1.grid(row=1,column=2)
#		self.b.place(x=10,y=10)
#		self.b1.place(x=10,y=50)
	def buttonclicked(self,num):
		if num==1:
			self.f['bg']='red'
		elif num==2:
			self.f['bg']='olive'
#		print('ho gya hai')
root=Tk()
m=myclass(root)
#m.b.bind('<Button-1>',m.buttonclicked(m.f))
root.mainloop()

