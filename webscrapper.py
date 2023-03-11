import socket
import urllib.request
file=urllib.request.urlopen('https://iul.ac.in')
content=file.read()
fs=open('demoscrapper.text','wb')
fs.write(content)
fs.close()

