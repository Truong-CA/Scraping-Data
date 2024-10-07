from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo WebDriver
driver = webdriver.Chrome()

# Mở trang Wikipedia
url = "https://en.wikipedia.org/wiki/List_of_acid_rock_artists"
driver.get(url)
time.sleep(5)

# Lấy tất cả các thẻ <ul>
ul_tags = driver.find_elements(By.TAG_NAME, "ul")

# In ra nội dung của tất cả các thẻ <ul>
for index, ul in enumerate(ul_tags):
    print(f"Thẻ ul số {index}: {ul.text[:100]}...")  # In 100 ký tự đầu tiên để dễ đọc
    print("-" * 50)

# Đóng WebDriver sau khi hoàn thành
driver.quit()
