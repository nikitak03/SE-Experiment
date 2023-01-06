#implementation of OTP Assignment as per OOP design
import random
import re
import smtplib

class sendotp:
    #constructor
    def __init__(self):
        try:
            self.server = smtplib.SMTP('smtp.gmail.com',587)
            self.server.ehlo()
            self.server.starttls()
            self.sender_email = 'nikitakadam025@gmail.com'
            self.sender_pass = 'sttdotqzbofyujtp'
            self.server.login(self.sender_email, self.sender_pass)
        except:
            print('unable to connect the server')
            exit()

        self.otp =None
        self.email = input('Enter receiver email: ')
        # self.email = email
        # self.length = length
        # self.validate_email()
        # x = self.generate_otp()
        # y = self.send_otp(x)

    # Method of Generation of otp

    def generate_otp(self,length):
        # otp_length = random.randint(4, 7)
        otp = ''
        for i in range(length):
            otp += str(random.randint(0,9))
        return otp


    # Method of Validation of email
    def validate_email(self):
        p = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if (re.search(p, self.email)):
            print("Given Email is valid.")

            return True
        else:
            print("Given Email is not valid!")

            return False

        # Method of Sending otp

    def send_otp(self):
        self.server.sendmail(self.sender_email, self.sender_pass, self.email, "Subject:your otp is: "+ self.otp)
        print('Otp has been sent to {}'.format(self.email))

if __name__ == '__main__':
    ob = sendotp()
    length = int(input('Enter the OTP length: '))
    ob.otp = ob.generate_otp(length)
    ob.validate_email()
    ob.send_otp()
    ob.server.close()

# length = random.randint(4,7)
# program1 = sendotp("sonukdm88@gmail.com",length)