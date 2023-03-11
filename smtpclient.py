import smtplib
from email.mime.text import MIMEText
body=input('enter the message :\n')
msg=MIMEText(body)
fromaddress='techshoaib7@gmail.com'
toaddress=input('enter mail id where has to be sent :\n')
msg['FROM']=fromaddress
msg['TO']=toaddress
msg['Subject']='test mail'
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddress,'Ammi@1234')
server.send_message(msg)
print('mail sent')
server.quit()
