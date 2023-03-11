import MySQLdb
con=MySQLdb.connect(host='localhost',database='boss',user='shoaib',password='admin@123')
cur=con.cursor()
e=input("enter your email\n")
p=input("enter your password\n")
s=int(input("enter your status\n"))
res='insert into user values(%s,%s,%s)'
#dlt='delete from user where(status=111)'
final=(e,p,s)
cur.execute(res,final)
con.commit()
cur.close()
con.close
