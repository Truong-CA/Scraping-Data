from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import re
import time

# toa dataframe
data = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})

# tao driver
driver = webdriver.Chrome()

# mo trang
url = "https://en.wikipedia.org/wiki/Edvard_Munch"
driver.get(url)

time.sleep(2)
# lay ten
try:
    name = driver.find_element(By.TAG_NAME, "h1").text
except:
    name = ""
# ngay sinh
try:
    birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
    birth = birth_element.text
    birth = re.findall(r'[0-9]{1,2} +\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]
except:
    birth = ""
# ngay mat
try:
    death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
    death = death_element.text
    death = re.findall(r'[0-9]{1,2}  +\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
except:
    death = ""
try:
    nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
    nationality = nationality_element.text
except:
    nationality = ""
# tao dic
painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}
# chuyen thanh dataframe
painter_df = pd.DataFrame([painter])
# them thong tin
data = pd.concat([data, painter_df], ignore_index=True)

#in
print(data)

#quit
driver.quit()