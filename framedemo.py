from tkinter import *
class demo:
	def buttonclicked(self):
		print('create successfully!')
	def __init__(self,root):
#		root=Tk()
		f=Frame(root,height=500,width=800,bg='blue',cursor='arrow')
		f.propagate(0)
		f.pack()
		b=Button(f,height=10,width=30,text='submit',bg='#bcbcbc',fg='#ececec')
		b.pack()
#		c=Label(f,b,height=10,width=30,text='firstname',bg='#bcbcbc',fg='#ececec')
#		c.pack()
#		c.bind('<Button-1>',demo.buttonclicked)
		b.bind('<Button-1>',demo.buttonclicked)
		root.mainloop()
root=Tk()
m=demo(root)
