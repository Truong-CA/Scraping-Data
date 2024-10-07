from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import pandas as pd
import getpass
from selenium.webdriver.common.action_chains import ActionChains

# Đường dẫn đến file thực thi geckodriver
gecko_path = r"C:/Users/Loc/Desktop/Ca DL/bài 2/geckodriver.exe"

# Khởi tởi đối tượng dịch vụ với đường geckodriver
ser = Service(gecko_path)

# Tạo tùy chọn
options = webdriver.firefox.options.Options();
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
# Thiết lập firefox chỉ hiện thị giao diện
options.headless = False

# Khởi tạo driver
driver = webdriver.Firefox(options=options, service=ser)

# Tạo url
url = 'https://www.reddit.com/login/'

# Truy cập
driver.get(url)

# Tạm dừng khoảng 2 giây
time.sleep(2)
#nhap thong tin ngyuoi dung
my_email= input('Please provide your email:')
my_password = getpass.getpass('Please provide your password')

#Dang nhap
#username_input =driver.find_element(By.XPATH,"//input[@id='login-username']")
#password_input =driver.find_element(By.XPATH,"//input[@id='login-password']")

# Nhap thong tin va nhan enter
#username_input.send_keys(my_email)
#password_input.send_keys(my_password + Keys.ENTER)
#time.sleep(5)
# Cách 2

# Đăng nhập
#username_input =driver.find_element(By.XPATH, "//input[@name='username']")
#password_input =driver.find_element(By.XPATH, "//input[@name='password']")

# Nhấn thông tin và nhấn nút Enter
#username_input.send_keys(my_email)
#password_input.send_keys(my_password + Keys.ENTER)
#time.sleep(5)

actionChains = ActionChains(driver)
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
time.sleep(1)
actionChains.send_keys(my_email).perform()
time.sleep(1)
actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys(my_password+Keys.ENTER).perform()
time.sleep(20)
# Truy cap trang post bai
url2 = 'https://www.reddit.com/submit?type=TEXT'
driver.get(url2);
time.sleep(2)

for i in range(16):
    actionChains.key_down(Keys.TAB).perform()
    time.sleep(1)

actionChains.send_keys('Vi du post').perform()

actionChains.key_down(Keys.TAB).perform()
actionChains.send_keys('Le Nhat Tung' + Keys.ENTER).perform()

for i in range(4):
    actionChains.key_down(Keys.TAB).perform()
    time.sleep(1)

actionChains.key_down(Keys.Enter).perform()

time.sleep(15)
driver.quit()
#button_login = driver.find_element(By.XPATH,"//button[text()='Log in']")
#button_login.click()

time.sleep(15)
driver.quit()
