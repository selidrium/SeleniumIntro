from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = "https://www.python.org/"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path="chromedriver.exe", log_path="NUL"))

driver.get(url)
element = driver.find_element(By.CLASS_NAME, 'shrubbery')

table = driver.find_element(By.CLASS_NAME, "event-widget")

date_list = table.find_elements(By.TAG_NAME, 'time')
event_list = table.find_element(By.CLASS_NAME, "menu").find_elements(By.TAG_NAME, 'a')

final_dict = {f"{i}": {"date": date_list[i].text, "name": event_list[i].text} for i in range(len(date_list))}

print(final_dict)

driver.quit()
