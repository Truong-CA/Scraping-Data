from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

######################################################
# I. Tạo danh sách chứa links và DataFrame rỗng
all_links = []
d = pd.DataFrame({'name of the band': [], 'year activity': []})

######################################################
# II. Lấy ra tất cả đường dẫn để truy cập đến nhạc sĩ bắt đầu bằng chữ "A"
# Khởi tạo WebDriver
driver = webdriver.Chrome()

url = "https://en.wikipedia.org/wiki/Lists_of_musicians"
try:
    # Mở trang
    driver.get(url)
    time.sleep(5)

    # Lấy ra tất cả các thẻ <a>
    a_tags = driver.find_elements(By.TAG_NAME, "a")

    links = []

    for tag in a_tags:
        try:
            link_text = tag.text
            href = tag.get_attribute("href")
            # Lọc liên kết bắt đầu với 'A' và chứa từ khóa "List of"
            if link_text.startswith("List of") and link_text[9].upper() == 'A':
                links.append(href)
                print(f"Found link: {href}")
        except Exception as e:
            print(f"Lỗi khi lấy thông tin từ thẻ <a>: {e}")
            continue

    # Kiểm tra và lấy link đầu tiên trong phần "A"
    if links:
        first_link = links[0]
        print(f"First link in 'A': {first_link}")
    else:
        print("No links found starting with 'A' and 'List of'")
        driver.quit()
        exit()

except Exception as e:
    print(f"Error loading page: {e}")
    driver.quit()

######################################################
# III. Lấy thông tin từ link đầu tiên trong phần 'A'
try:
    driver.get(first_link)
    time.sleep(2)

    # Lấy tên ban nhạc từ tiêu đề trang
    try:
        name = driver.find_element(By.TAG_NAME, "h1").text
    except Exception as e:
        name = ""
        print(f"Error retrieving band name: {e}")

    # Lấy năm hoạt động
    try:
        year_activity_element = driver.find_element(By.XPATH, "//th[text()='Years active']/following-sibling::td")
        year_activity = year_activity_element.text
    except Exception as e:
        year_activity = ""
        print(f"Error retrieving years active: {e}")

    # Tạo dictionary thông tin
    musician = {'name of the band': name, 'year activity': year_activity}

    # Chuyển thành DataFrame và thêm vào DataFrame chính
    musician_df = pd.DataFrame([musician])
    d = pd.concat([d, musician_df], ignore_index=True)

except Exception as e:
    print(f"Error processing musician page: {e}")

######################################################
# IV. Lưu kết quả vào file Excel
file_name = 'musicians.xlsx'
d.to_excel(file_name, index=False)
print(f"DataFrame is written to Excel file '{file_name}' successfully.")

# Đóng WebDriver
driver.quit()
