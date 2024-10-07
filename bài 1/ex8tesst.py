from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

######################################################
# I. Tạo danh sách chứa links và DataFrame rỗng
all_links = []
d = pd.DataFrame({'name_of_the_band': [], 'year_activity': []})

######################################################
# II. Lấy ra tất cả đường dẫn để truy cập đến nghệ sĩ
# Khởi tạo Webdriver
driver = webdriver.Chrome()

url = "https://en.wikipedia.org/wiki/Lists_of_musicians"
try:
    # Mở trang
    driver.get(url)
    time.sleep(5)

    # Lấy ra tất cả các thẻ ul
    ul_tag = driver.find_elements(By.TAG_NAME, "ul")

    # Chọn thẻ ul thứ 21
    if len(ul_tag) > 21:
        ul_musicans = ul_tag[21]  # ul ngoài

        # Lấy ra tất cả các thẻ <li> thuộc ul_musicans
        li_tags_ul1 = ul_musicans.find_elements(By.TAG_NAME, "li")

        links = []

        def extract_links_in_ul2(li_elements):
            """Hàm này để duyệt tất cả các thẻ <li> trong ul2 của từng thẻ <li> thuộc ul1"""
            for li in li_elements:
                try:
                    # Lấy thẻ <a> trong mỗi <li> nếu có
                    link = li.find_element(By.TAG_NAME, "a").get_attribute("href")
                    links.append(link)
                except Exception as e:
                    print(f"Lỗi khi lấy thông tin từ thẻ <li> trong ul2: {e}")
                    continue

        def process_ul1_and_ul2(li_elements):
            """Hàm để xử lý các thẻ <li> của ul1 và truy cập vào ul2 nếu có"""
            for li in li_elements:
                try:
                    # Lấy thẻ <a> trong <li> của ul1 nếu có
                    link = li.find_element(By.TAG_NAME, "a").get_attribute("href")
                    links.append(link)

                    # Kiểm tra xem thẻ <li> này có chứa thẻ <ul> con (ul2) hay không
                    ul2 = li.find_elements(By.TAG_NAME, "ul")
                    if ul2:
                        # Nếu có <ul2>, duyệt qua các thẻ <li> trong ul2
                        li_tags_ul2 = ul2[0].find_elements(By.TAG_NAME, "li")
                        extract_links_in_ul2(li_tags_ul2)

                except Exception as e:
                    print(f"Lỗi khi lấy thông tin từ thẻ <li> của ul1: {e}")
                    continue

        # Gọi hàm để duyệt qua ul1 và nếu có ul2 trong các thẻ <li>, thì xử lý tiếp
        process_ul1_and_ul2(li_tags_ul1)

        all_links.extend(links)  # dùng extend để không tạo danh sách lồng
    else:
        print("Không tìm thấy các thẻ ul với chỉ số mong muốn.")

except Exception as e:
    print(f"Error: {e}")

######################################################
# III. Lấy thông tin của từng nghệ sĩ
for link in all_links:
    try:
        driver.get(link)
        time.sleep(2)

        # Lấy tên nghệ sĩ
        try:
            name_of_the_band = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name_of_the_band = ""

        # Lấy năm hoạt động
        try:
            yearactivitys_element = driver.find_element(By.XPATH, "//th[text()='Years active']/following-sibling::td")
            yearactivitys = yearactivitys_element.text
        except:
            yearactivitys = ""

        # Tạo dictionary thông tin của nghệ sĩ
        musician = {'name_of_the_band': name_of_the_band, 'year_activity': yearactivitys}

        # Chuyển đổi dictionary thành DataFrame và thêm vào DataFrame chính
        musician_df = pd.DataFrame([musician])
        d = pd.concat([d, musician_df], ignore_index=True)

    except Exception as e:
        print(f"Error khi xử lý link: {e}")

######################################################
# IV. In thông tin
print(d)

# Đặt tên file
file_name = 'Nguyen_Duc_Truong_Lists_of_musicians.xlsx'

# Lưu vào file Excel
d.to_excel(file_name, index=False)  # index=False để không lưu chỉ số
print('DataFrame is written to Excel file successfully.')

# Đóng webdriver sau khi lấy thông tin
driver.quit()
