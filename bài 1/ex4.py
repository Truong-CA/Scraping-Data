from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# khỏi tao 1 webdriver
driver = webdriver.Chrome()

# Mơ
url = "https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22P%22"

driver.get(url)

# đợi một chút để trang tải
time.sleep(2)

# lấy ra tất cả ca thể ul
ul_tags =driver.find_elements(By.TAG_NAME, "ul")

# choọn the vi thứ 21
ul_painters = ul_tags[20]  # list bắt đầu index bằng 0, bắt đầu lấy từ 1

# tìm ul
#print(len(ul_tags))
#for ul_tag in ul_tags:
#   print(ul_tag.get_attribute())



# Lấy ra tất cả th <li> thuộc ul_painters
li_tags = ul_painters.find_elements(By.TAG_NAME,"li")

# tạo danh sách caác url
Links = [tag.find_element(By.TAG_NAME,"a").get_attribute("href") for tag in li_tags]

# tạo danh sách các url
titles= [tag.find_element(By.TAG_NAME,"a").get_attribute("title") for tag in li_tags]

# in ra url
for link in Links:
    print(link)
for title in titles:
    print(title)

# đóng web
driver.quit()