# -*-encoding:utf-8 -*-
#newemail.py
import smtplib
from email.mime.text import MIMEText
def prompt(prompt):
    return input(prompt).strip()
 
#POP3host=prompt('POP3host:')
toaddr=prompt('TO:')
username=prompt('Username:')
passw=prompt('Password:')
fromaddr=username+'@163.com'
msgtext=('From:%s\r\nTo:%s\r\n\r\n'%(fromaddr,toaddr))
while 1:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msgtext = msgtext + line
	
msg=MIMEText(msgtext,"plain")
msg['Subject']="test subject"
server=smtplib.SMTP('smtp.163.com:25')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,passw)
server.sendmail(fromaddr,toaddr,msg.as_string())
server.quit()