from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import requests

# Tọa dataframe rong
data= pd.DataFrame({'name' : [], 'birth': [],'death': [], 'nationality': []})

# khỏi tạo web driver
driver = webdriver.Chrome()

# mo tang
url= "https://en.wikipedia.org/wiki/Edvard_Munch"
driver.get(url)

# đợi 2 fiaay
time.sleep(2)
# Lấy tên cuủ hao si
try:
    name= driver.find_element(By.TAG_NAME,"h1").text

except:
    name= ""

# Lấy ngày sinh
try:
    birth_element = driver.find_element(By.XPATH, "//th[text() = 'Born'/following-sibling::td")
    birth=birth_element.text
    birth =re.findall(r'[0-9]{1,2}+\s[A-Za-z]+\s+[0-9]{4}',birth)[0]

except:
    birth= ""

# lấy ngày mất
try:
    death_element = driver.find_element(By.XPATH, "//th[text() = 'Die'/following-sibling::td")
    death=death_element.text
    birth =re.findall(r'[0-9]{1,2} +\s[A-Za-z]+\s+[0-9]{4}',death)[0]

except:
    death= ""

# Lấy quốc tịch
try:
    nationality_element = driver.find_element(By.XPATH, "//th[text() = 'Nationality'/following sibling::td")
    nationality=nationality_element.text


except:
    nationality= ""

# tạo ra dictionary thanh dataframe
painter = {'name' : name, 'birth': birth,'death': death, 'nationality': nationality}
painter_df =pd.DataFrame([painter])

# them thông tin vào DF chính
data= pd.concat([data,painter_df], ignore_index=True)
# in
print(data)
# quit
driver.quit()
