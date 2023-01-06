import random
import smtplib
n=(int(input("Enter your range of otp ")))
def generate_otp(n):
    OTP=""
    for i in range(n):
        OTP+=str(random.randint(0,9))
    return (OTP)
server =smtplib.SMTP('smtp.gmail.com',587)

Senders_email = 'nikitakadam025@gmail.com'
Senders_password= 'nikita@9075263711'

def login_into_sendersemail():
    server.starttls()
    server.login('nikitakadam025@gmail.com',password='sttdotqzbofyujtp')
receivers_name=input("Enter receivers name ")
receivers_email=input("Enter receivers email ")
def send_email():
    login_into_sendersemail()
    otp_var=generate_otp(n)
    msg=("Hi "+ receivers_name +"\n"+ str(otp_var)+" is your OTP ")
    print(msg)
    server.sendmail(Senders_email,receivers_email,msg)
    server.quit()
    print("email has been sent!")
send_email()
