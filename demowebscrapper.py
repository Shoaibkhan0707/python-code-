import socket
#import urllib.request
import urllib.request
web= urllib.request.urlopen('https://www.youtube.com/user/guru99com')
print("result code " + str(web.getcode()))
data=web.read()
print(data)
