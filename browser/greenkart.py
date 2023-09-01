import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()  # Service Manager
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
# Max wait time is 5sec ...2sec(3sec save)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum=0
for price in prices:
    sum=sum+int(price.text)

print(sum)
totalamount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(totalamount)
assert sum==totalamount

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# Explicitwait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

dropdown = Select(driver.find_element(By.XPATH, "//div[@class='wrapperTwo']//div//select"))
dropdown.select_by_value("India")

driver.find_element(By.CSS_SELECTOR, ".chkAgree").click()

driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']").click()

message = driver.find_element(By.XPATH,
                              "//span[contains(text(),'Thank you, your order has been placed successfully')]").text
print(message)
driver.close()
