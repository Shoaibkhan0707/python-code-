from zipfile import *
f=zipfile('myzip.zip','w',ZIP_DEFLATED)
f.write('sample.txt')
#f.write('abc.text')
#f.write('global.py')
f.close()
