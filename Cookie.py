# Automate the Cookie Clicker game
# Purchases the most expensive items automatically to maximize profit

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Selenium Setup
url = "http://orteil.dashnet.org/experiments/cookie/"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("window-size=1200x600")

driver = webdriver.Chrome(options=options, service=Service(executable_path="chromedriver.exe", log_path="NUL"))
driver.get(url)

# Element Set Up
cookie = driver.find_element(By.ID, 'cookie')
cookie_click = driver.find_element(By.XPATH, '//*[@id="cookie"]')
store = driver.find_element(By.XPATH, '//*[@id="store"]')
items = store.find_elements(By.TAG_NAME, 'div')
div_list = []

# Retrived Element Attributes into a list
for item in reversed(items):
    div_list.append(item.get_attribute('id'))
    print(item)


def check_cookies():
    for i in range(len(div_list)):
        try:
            store.find_element(By.ID, div_list[i]).click()
        except:
            print("ElementNotInteractableException")
        finally:
            pass


start_time = time.perf_counter()
while True:
    cookie.click()

    current_time = time.perf_counter()
    if current_time - start_time > 5:
        print("function!")
        check_cookies()
        start_time = current_time

# driver.quit()
