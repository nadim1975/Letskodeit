from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest
import time

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.lp= LoginPage(self.driver)


    @pytest.mark.run(order=2)
    def test_validlogin(self):
        self.lp.login('test@email.com','abcabc')
        result = self.lp.verifyLoginSuccessful()
        assert result == True


    @pytest.mark.run(order = 1)
    def test_invalidlogin(self):
        # The class Setup fixture will open the URL the first time
        self.lp.login('test@email.com','abc')
        result = self.lp.verifyLoginFailure()
        assert result == True





