import MySQLdb
con=MySQLdb.connect(host='localhost',database='boss',user='shoaib',password='admin@123')
cur=con.cursor()
cur.execute('select * from user')
row=cur.fetchone()
while row is not None:
#rows=cur.fetchall()
#        print(cur.rowcount) # count how many lines:
#for row in rows:
        #print(row[1]) print only index 1: -> inter
        print(row) # print all line
        row=cur.fetchone()
cur.close()
con.close()

