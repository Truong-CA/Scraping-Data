from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#
driver = webdriver.Chrome()
#
driver.get("http://gomotungkinh.com")
time.sleep(5)


bonk_img = driver.find_element(By.ID,"bonk")

# click lien tuc vao img " bonk"
while True:
    bonk_img.click()
    print("Clicked on the bonk image")
    time.sleep(2)