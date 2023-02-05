from selenium import webdriver
from selenium.webdriver.common.by import By

#.exe 안 넣어도 됨
chrome_driver_path = r"C:\Users\JDoubleU\Desktop\chromedriver\chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")


event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
  events[n] = {
    "time":event_times[n].text,
    "name":event_names[n].text
  }

print(events)

driver.quit() # 단일 텝
# driver.quit() # 모든 텝
