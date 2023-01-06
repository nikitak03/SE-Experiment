import unittest
import MYOTP

class TestStringMethods(unittest.TestCase):

    def testcase1(self):
        Email = MYOTP.validate_email('aditya.mote10@gmail.com')
        self.assertEquals(True,Email)

    def testcase2(self):
        size = 4
        Email = MYOTP.generate_otp()
        self.assertEqual(len(Email), size)

    def testcase3(self):
        Email = MYOTP.send_mail(MYOTP.generate_otp())
        self.assertEquals(True,Email)

    # def testcase4(self):
    #     size = 4
    #
    #     Email = MYOTP.emailsender
    #     self.assertIn("@", Email)
    #     self.assertIn(".", Email)
    #     self.assertIn("com", Email)
    #
    #     res = MYOTP.otp(4)
    #     self.assertEqual(len(res), size)

if __name__ == '__main__':
    unittest.main()