def add():
	a=int(input("enter the number"));
	b=int(input("enter the number"));
	c=a+b
	print(c)
def sub():
        a=int(input("enter the number"));
        b=int(input("enter the number"));
        c=a-b
        print(c)
def mul():
        a=int(input("enter the number"));
        b=int(input("enter the number"));
        c=a*b
        print(c)
def div():
        a=int(input("enter the number"));
        b=int(input("enter the number"));
        c=a/b
        print(c)
def call():
	while(1):
		print("option\n")
		option=(int(input("option\n 1.add\n 2.sub\n 3.mul\n 4.div\n 5.exit\n")))
		if option==1:
			add()
		if option==2:
			sub()
		if option==3:
			mul()
		if option==4:
			div()
		if option==5:
			return 0
		if option>5:
			print("invalid option")

call()


