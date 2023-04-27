from selenium import webdriver
from Pages.LoginPage import *
from Pages.HomePage import *
import Locators.id as Users
class Login_Script():

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        login = LoginPage(self.driver)
        login.enterUsername(Users.mf.username)
        login.enterPassword(Users.mf.password)
        login.clickLoginButton()

        homepage = HomePage(self.driver)
        homepage.confirmLogin()