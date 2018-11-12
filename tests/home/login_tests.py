from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validlogin(self):
        baseURL = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        driver.maximize_window()
        lp = LoginPage(driver)
        lp.login('test@email.com','abcabc')
        loginIcon = driver.find_element(By.XPATH,"//*[@id='navbar']//span[text()='Test User']")

        if loginIcon is not None:
            print('login successful')
        else:
            print ('failed to login')









