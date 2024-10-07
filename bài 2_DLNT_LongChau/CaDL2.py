

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
# Đường dẫn đến file thực thi geckodriver
gecko_path = r"C:/Users/Loc/Desktop/Ca DL/bài 2/geckodriver.exe"

# Khowi taạo đối tượng dịch vụ toi duong dan geckodriver
ser = Service(gecko_path)

# Tao tuy chon
options = webdriver.firefox.options.Options()
options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"
# Thieets lap firefox chi hien thi giao dien
options.headless = False

# Khowir tao driver
driver = webdriver.Firefox(options = options, service=ser)

# taoj url
url= "http://pythonscraping.com/pages/javascript/ajaxDemo.html"

# truy capaj
driver.get(url)

# In ra moi dung cua trang web
print("Before ___________________________________ \n")
print(driver.page_source)


# Tam dung khoang 3s
time.sleep(3)

# In lai

print("\n\n\n\n After: _______________________________________ \n")
print(driver.page_source)

# Dong browser
driver.quit()
