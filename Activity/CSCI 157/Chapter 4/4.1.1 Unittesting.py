import unittest
__author__ = 'Fossum'


class User():
    def __init__(self, username, email, SS, password):
        self.username = username
        self.email = Email(email)
        self.ssn = Social(SS)
        self.hash = Hash(password)

    def check_password(self, password_check):
        return self.hash == Hash(password_check)

    def __str__(self):
        header = "The user " + self.username + " has the email " + str(self.email) +\
                 " and a social security number of " + str(self.ssn) + "."
        return header


class FixturesTest(unittest.TestCase):

    def setUp(self):
        print("In setUp()")
        self.fixture = User("Justin", "jcf3@alfred.edu", "111-11-1111", "ThIsIsMyPaSsWoRd")

    def tearDown(self):
        print("In tearDown()")
        del self.fixture

    def test(self):
        print("In test()")
        self.assertEqual(self.fixture.username(), "Justin")
        self.assertEqual(self.fixture.email(), "jcf3@alfred.edu")
        self.assertEqual(self.fixture.ssn(), "111-11-1111")
        self.assertEqual(self.fixture.hash(), "ThIsIsMyPaSsWoRd")
        self.assertFalse(self.fixture.check_password("password"))
        self.assertEqual(self.fixture.__str__(), "The user Justin has the email jcf3@alfred.edu and a social security"
                                                 "number of 111-11-1111.")

if __name__ == '__main__':
    unittest.main()
