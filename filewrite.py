filename="filewrite.text"
filename="copywrite"
flag=True
with open(filename,'a')as ftw:
	print('enter the line,to quit type.quit')
	while flag:
		data=input()
		if data.__ne__('quit'):
			ftw.write(data+'\n')
		else:
			flag=False
