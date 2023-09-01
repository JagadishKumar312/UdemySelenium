from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
radiobuttons=driver.find_elements(By.CSS_SELECTOR,".radioButton")
print(len(radiobuttons))
radiobuttons[2].click()
assert radiobuttons[2].is_selected()
time.sleep(2)
assert (driver.find_element(By.ID,"displayed-text").is_displayed())
driver.find_element(By.ID,"hide-textbox").click()
assert not (driver.find_element(By.ID,"displayed-text").is_displayed())

