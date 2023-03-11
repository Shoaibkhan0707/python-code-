import socket
host='localhost'
#TCP_IP='127.0.0.1'
port=5005
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
print("connection from :",str(addr))
c.send(b'hello how are you\n')
msg='bye!'
c.send(msg.encode())
c.close()
