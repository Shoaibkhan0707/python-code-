import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr=socket.gethostbyname('www.facebook.com')
print(addr)
