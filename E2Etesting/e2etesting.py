import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, " a[href*='shop']").click()
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
time.sleep(2)
for product in products:
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".btn.btn-success").click()
driver.find_element(By.ID,"country").send_keys("Ind")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".checkbox.checkbox-primary").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()
message=driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(message)
time.sleep(2)
driver.close()
