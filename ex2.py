from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# khỏi tao 1 webdriver
driver = webdriver.Chrome()

# Mơ
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name"
driver.get(url)

# đợi khoảng 2s
time.sleep(2)

# lấy tất cả các tht
tags = driver.find_elements(By.TAG_NAME, value = "a")
 # tạo ra danh sách liên kết
links= [tag.get_attribute("href") for tag in tags]
for link in links:
    print(link)
driver.quit()
