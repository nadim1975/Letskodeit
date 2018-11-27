from pages.home.login_page import LoginPage
import unittest
from utilities.teststatus import TestStatus
import pytest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.lp= LoginPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_validlogin(self):
        result1 = self.lp.verifyLoginPageTitle("Let'sKode It")
        self.ts.mark(result1,'Title is incorrect')
        self.lp.login('test@email.com','abcabc')
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("Validating Login",result2,"Login was successful")


    @pytest.mark.run(order = 1)
    def test_invalidlogin(self):
        # The class Setup fixture will open the URL the first time
        self.lp.login('test@email.com','abc')
        result = self.lp.verifyLoginFailure()
        self.ts.mark(result,"Couldn't login with wrong userid/password")



