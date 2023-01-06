#Task-1: Implement a program in Java/Python to generate One Time Password and send it to the
#registered email ID or mobile number.

#1.Generate OTP ---- By using Random Module
#2.Send OTP to Users email address ---- Smptlib Module
#smptlib stands for Simple Mail Transfer Protocol client
# Four Digit OTP ---- 1245,8975,3647

import random
import smtplib

#otp = ''.join([str(random.randint(0,9)) for i in range(4)])
#print(otp)

server = smtplib.SMTP('smtp.gmail.com',587)

#print(server)

server.starttls()
server.login('nikitakadam025@gmail.com','sttdotqzbofyujtp')
otp = ''.join([str(random.randint(0,9)) for i in range(4)])

msg="Hello, Your OTP is "+str(otp)
server.sendmail('nikitakadam025@gmail.com','sonukdm88@gmail.com',msg)
server.quit()