from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage():

    def test_validlogin(self):
        baseURL = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        driver.maximize_window()

        loginLink = driver.find_element(By.LINK_TEXT,"Login")
        loginLink.click()

        emailAddress = driver.find_element(By.ID,'user_email')
        emailAddress.send_keys('test@email.com')

        password = driver.find_element(By.ID,'user_password')
        password.send_keys('abcabc')

        loginButton = driver.find_element(By.NAME,"commit")
        loginButton.click()

        loginIcon = driver.find_element(By.XPATH,"//*[@id='navbar']//span[text()='Test User']")

        if loginIcon is not None:
            print('logged in successfully')
        else:
            print ('failed to login')



c = LoginPage()
c.test_validlogin()







