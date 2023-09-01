import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# xpath,CSS,ID,classname,linktext
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
time.sleep(2)
driver.find_element(By.XPATH," //form/div[1]/input").send_keys("demo@gmail.com")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello123")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello123")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()



