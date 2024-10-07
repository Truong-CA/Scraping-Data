from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
import time
import pandas as pd
import getpass
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

# Tạo url
url = 'https://vi-vn.facebook.com/login/'

# Truy cập
driver.get(url)
time.sleep(3)

# Nhap thong tin nguoi dung
my_email = input('Please provide your email:')
my_password = getpass.getpass('Please provide your password:')

actionChains = ActionChains(driver)
actionChains.send_keys(my_email).perform()
actionChains.key_down(Keys.TAB).perform()

actionChains.send_keys(my_password + Keys.ENTER).perform()
time.sleep(10)
for i in range(15):
    actionChains.key_down(Keys.TAB).perform()
actionChains.key_down(Keys.ENTER)
actionChains.key_down(Keys.ENTER)
actionChains.send_keys('Thực hành Cào dữ liệu facebook').perform()
for i in range(10):
    actionChains.key_down(Keys.TAB).perform()
actionChains.key_down(Keys.ENTER)
actionChains.key_down(Keys.ENTER)



time.sleep(10)
driver.quit()