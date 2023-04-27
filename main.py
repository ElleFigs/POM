from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
from Scripts.LoginScript import *
from Scripts.MenuNavigation import *

import time

# Command Prompt to code in existing window
# cd "C:\Program Files\Google\Chrome\Application"
# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\MichaelFigelman\.spyder-py3\Screen recorder"


opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=opt)
driver.get("https://apps.nextworld.net")

login = Login_Script(driver)
login.login()

navigation = MenuNavigation_Script(driver)
navigation.changeZones('appdevauto.master', 'autotest')

