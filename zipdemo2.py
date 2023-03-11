from zipfile import ZipFile
f=ZipFile('myzip.zip','r')
f.extractall()
f.close()
