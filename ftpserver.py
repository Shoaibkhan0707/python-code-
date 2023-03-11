import socket
host='localhost'
port=6769
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print('server accepted connection')
fname=c.recv(1024)
fname=str(fname.decode())
print('received filename from client',fname)
try:
	f=open(fname,'rb')
	content=f.read()
	c.send(content)
	print('file sent')
	f.close()
except:
	c.send(b'file not found')
c.close()
