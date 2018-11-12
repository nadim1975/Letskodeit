from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    # constructor method to pass values
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    # Locators
    _login_link = "Login"
    _email_field = 'user_email'
    _password_field = 'user_password'
    _login_button = "commit"

    # Methods to expose elements (
    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT,self._login_link)
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID,self._email_field)
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID,self._password_field)
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME,self._login_button)

    # Methods to perform actions on elements
    def clickLoginLink(self):
        self.elementClick(self._login_link,'link')
    def enterEmail(self,email):
        self.sendKeys(email,self._email_field)
    def enterPassword(self,password):
        self.sendKeys(password,self._password_field)
    def clickLoginButton(self):
        self.elementClick(self._login_button,'name')

    #Main Method
    def login(self,email,password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
