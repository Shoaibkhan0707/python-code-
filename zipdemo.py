from zipfile import ZipFile
f=ZipFile('myzip.zip','w')
f.write('sample.txt')
f.write('abc.text')
#f.write('global.py')
f.close()
