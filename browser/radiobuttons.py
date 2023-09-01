from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

radios = driver.find_elements(By.XPATH, "//div[@id='radio-btn-example']/fieldset/label")
print(len(radios))

for radio in radios:
    if radio.get_attribute("for") == "radio3":
        radio.click()
        print("radio button clicked")
        break

time.sleep(2)