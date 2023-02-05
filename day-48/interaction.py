from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = r"./Cchromedriver_win32/chromedriver"
driver = webdriver.Chrome()

url = 'https://www.naver.com/'
driver.get(url)

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # article_count.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Talk")
# print(all_portals)
# print(all_portals.text)
# print(all_portals.click())

#네이버 아이디 입력창 접속
anchor = driver.find_element(By.CSS_SELECTOR, "#account a")
anchor.click()

id_input = driver.find_element(By.CSS_SELECTOR, "#id")
id_input.send_keys("whd7327")

passwd_input = driver.find_element(By.CSS_SELECTOR, "#pw")
passwd_input.send_keys("")

anchor.find_element(By.CSS_SELECTOR, "#log.login").click()

try:
    # 브라우저를 최대 10초까지 기다린다. (xpath의 값이 나올때까지)
    elem = WebDriverWait(driver, 20).until(
    	EC.presence_of_element_located((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))
    )
    print(elem.text)
finally:
    driver.quit()
