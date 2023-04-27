from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.usernameId = 'username-landing'
        self.passwordId = 'password-landing'
        self.loginButtonId = 'loginbtn'

    def enterUsername(self, username):
        counter = 0
        while True:
            try:
                self.driver.find_element(By.ID, self.usernameId).clear()
                self.driver.find_element(By.ID, self.usernameId).send_keys(username)
                break
            except (NoSuchElementException, NoSuchWindowException, StaleElementReferenceException, ElementNotInteractableException):
                time.sleep(1)
                counter += 1
                if counter != 6:
                    strCounter = str(counter)
                    print(f'Tried to find clickable object {strCounter} number of times ')
                else:
                    print('Not trying to find object anymore')
                    break
                pass

    def enterPassword(self, password):
        counter = 0
        while True:
            try:
                self.driver.find_element(By.ID, self.passwordId).clear()
                self.driver.find_element(By.ID, self.passwordId).send_keys(password)
                break
            except (NoSuchElementException, NoSuchWindowException, StaleElementReferenceException,
                    ElementNotInteractableException):
                time.sleep(1)
                counter += 1
                if counter != 6:
                    strCounter = str(counter)
                    print(f'Tried to find clickable object {strCounter} number of times ')
                else:
                    print('Not trying to find object anymore')
                    break
                pass

    def clickLoginButton(self):
        counter = 0
        while True:
            try:
                self.driver.find_element(By.ID, self.loginButtonId).click()
                break
            except (NoSuchElementException, NoSuchWindowException, StaleElementReferenceException,
                    ElementNotInteractableException):
                time.sleep(1)
                counter += 1
                if counter != 6:
                    strCounter = str(counter)
                    print(f'Tried to find clickable object {strCounter} number of times ')
                else:
                    print('Not trying to find object anymore')
                    break
                pass



