from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
name = "jag"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
driver.find_element(By.ID, "name").send_keys(name)
time.sleep(2)
driver.find_element(By.ID, "alertbtn").click()
time.sleep(2)
alert = driver.switch_to.alert
alertxt= alert.text
print(alertxt)
assert name in alertxt
alert.accept()
driver.find_element(By.ID,"confirmbtn").click()
alertxt1=alert.text
print(alertxt1)
time.sleep(2)
alert.dismiss()

time.sleep(2)

