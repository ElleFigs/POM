import subprocess
from Scripts.LoginScript import *
import time

# Command Prompt to code in existing window
# cd "C:\Program Files\Google\Chrome\Application"
# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Users\MichaelFigelman\.spyder-py3\Screen recorder"

chromeDir = 'C:\\Program Files\\Google\\Chrome\\Application'
app = 'chrome.exe '
debugPort = '--remote-debugging-port=9222 '
directory = '--user-data-dir="C:\\Users\\MichaelFigelman\\.spyder-py3\\Screen recorder"'

# while True:
#     subprocess.run(app+debugPort+directory, shell=True, cwd=chromeDir)
#     break

try:
    output = subprocess.run(app+debugPort+directory, shell=True, cwd=chromeDir)
    print(output)
except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")
