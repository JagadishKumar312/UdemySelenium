import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox'] ")
len(checkboxes)

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break
time.sleep(2)

radios = driver.find_elements(By.XPATH, "//div[@id='radio-btn-example']/fieldset/label")
len(radios)
for radio in radios:
    if radio.get_attribute("for") == "radio3":
        radio.click()
        print("radio button clicked")
        break

time.sleep(2)
