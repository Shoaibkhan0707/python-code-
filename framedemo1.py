from tkinter import *
#class demo:
def buttonclicked(self):
	print('create successfully!')
def bluecolour(f):
	f['bg']='blue'
def redcolour(f):
	f['bg']='red'
root=Tk()
f=Frame(root,height=500,width=800,bg='blue',cursor='arrow')
#	f.propagate(0)
f.pack()
b=Button(f,height=10,width=30,text='submit',bg='#bcbcbc',fg='#ececec')
b.pack()
b.bind('<Button-1>',buttonclicked)
bb=Label(f,height=5,width=10,text='firstname',bg='#bcbcbc',fg='#ececec')
bb.pack()
#	b.bind('<Button-1>',buttonclicked)
bb.bind('<Button-1>',buttonclicked)
root.mainloop()
