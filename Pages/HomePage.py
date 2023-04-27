from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.NwLogoXPath = '//*[@id="homelink"]/span/img[1]'
        self.ZoneId = 'zones'
        self.FilterXPath = '//*[@id="nwBody"]/div[2]/div/div/div/div[2]/nw-table/div/div[1]/table/thead/tr[2]/th[2]/div/nw-dt-filter/span/span/span/input'
        self.TenantFilterXPath = '//*[@id="nwBody"]/div[2]/div/div/div/div[2]/nw-table/div/div[1]/table/thead/tr[2]/th[3]/div/nw-dt-filter/span/span/span/input'
        self.AppDevAutoMasterAutoTestXPath = '//*[@id="nwBody"]/div[2]/div/div/div/div[2]/nw-table/div/div[2]/table/tbody/tr[1]/td[1]'

    def confirmLogin(self):
        counter = 0
        while True:
            try:
                self.driver.find_element(By.XPATH, self.NwLogoXPath)
                time.sleep(1)
                print("Successful log in")
                break
            except (NoSuchElementException, NoSuchWindowException, StaleElementReferenceException, ElementNotInteractableException):
                time.sleep(1)
                counter += 1
                if counter != 6:
                    strCounter = str(counter)
                    print(f'Tried to find nw logo {strCounter} number of times ')
                else:
                    print('Not trying to find object anymore')
                    break
                pass

    def OpenEnvironment(self):
        counter = 0
        while True:
            try:
                self.driver.find_element(By.ID, self.ZoneId).click()
                time.sleep(1)
                break
            except (NoSuchElementException, NoSuchWindowException, StaleElementReferenceException,
                    ElementNotInteractableException):
                time.sleep(1)
                counter += 1
                if counter != 6:
                    strCounter = str(counter)
                    print(f'Tried to find nw logo {strCounter} number of times ')
                else:
                    print('Not trying to find object anymore')
                    break
                pass

    def typeNewEnvironment(self, environment):
        counter = 0
        while True:
            try:
                self.driver.find_element(By.XPATH, self.FilterXPath).send_keys(environment)
                time.sleep(1)
                break
            except (NoSuchElementException, NoSuchWindowException, StaleElementReferenceException,
                    ElementNotInteractableException):
                time.sleep(1)
                counter += 1
                if counter != 6:
                    strCounter = str(counter)
                    print(f'Tried to find nw logo {strCounter} number of times ')
                else:
                    print('Not trying to find object anymore')
                    break
                pass

    def typeNewTenant(self, tenant):
        counter = 0
        while True:
            try:
                ele = self.driver.find_element(By.XPATH, self.TenantFilterXPath)
                ActionChains(self.driver).send_keys_to_element(ele, tenant).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
                time.sleep(1)
                break
            except (NoSuchElementException, NoSuchWindowException, StaleElementReferenceException,
                    ElementNotInteractableException):
                time.sleep(1)
                counter += 1
                if counter != 6:
                    strCounter = str(counter)
                    print(f'Tried to find nw logo {strCounter} number of times ')
                else:
                    print('Not trying to find object anymore')
                    break
                pass

    def selectAutoTestTenant(self):
        counter = 0
        while True:
            try:
                ele = self.driver.find_element(By.XPATH, self.AppDevAutoMasterAutoTestXPath)
                if ele.text == 'AppDevAuto.master':
                    ActionChains(self.driver).double_click(ele).perform()
                else: print("can't find appdevauto.master")
                time.sleep(1)
                break
            except (NoSuchElementException, NoSuchWindowException, StaleElementReferenceException,
                    ElementNotInteractableException):
                time.sleep(1)
                counter += 1
                if counter != 6:
                    strCounter = str(counter)
                    print(f'Tried to find nw logo {strCounter} number of times ')
                else:
                    print('Not trying to find object anymore')
                    break
                pass