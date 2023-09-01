import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT, "Job Support").click()
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("jagadish")
time.sleep(3)
driver.close()