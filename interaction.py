from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://en.wikipedia.org/wiki/Main_Page"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path="chromedriver.exe", log_path="NUL"))

driver.get(url)
# element = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
element = driver.find_element(By.CSS_SELECTOR, '#articlecount a').text
link_text = driver.find_element(By.LINK_TEXT, "All Portals")
print(element)

driver.quit()