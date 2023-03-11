from  tkinter import *
class myclass:
	def buttonchecked(self):
		print('mission completed!')
	def __init__(self,root):
		f=Frame(root,height='500',width='800',bg='skyblue',cursor='arrow')
		f.propagate(0)
		f.pack()
		b=Button(f,height='10',width='30',text='submit',bg='#bcbcbc',fg='#ececec')
		b.pack()
		b.bind('<Button-1>',myclass.buttonchecked)
		root.mainloop()
root=Tk()
m=myclass(root)
