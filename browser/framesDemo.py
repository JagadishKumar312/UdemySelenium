import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
time.sleep(2)
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate the frames")
time.sleep(2)
driver.switch_to.default_content()
time.sleep(2)
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
