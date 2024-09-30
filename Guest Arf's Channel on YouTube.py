from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

import sys

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.youtube.com/@guestarf9875") #put website here

for i in range(0,1000000000): #keeps window open for as long as possible
    time.sleep(100)
    time.sleep(100)
    time.sleep(100)
    time.sleep(100)

locate_python = sys.exec_prefix

print(locate_python)

sys.exit()