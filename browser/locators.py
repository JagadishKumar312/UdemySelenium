import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

# xpath,CSS,ID,classname,linktext
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("JAgadish")
time.sleep(3)
driver.find_element(By.NAME, "email").send_keys("jaggu.career@gmail.com")
time.sleep(3)
print("mail entered")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("adf123")
time.sleep(3)
print("password entered")
driver.find_element(By.ID, "exampleCheck1").click()
time.sleep(3)

#Static dropdown
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")
time.sleep(2)


# for xpath //tagname[@attribute='value']
# for CSS selector tagname[attribute='value'] # for id         . for class
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
time.sleep(1)

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Data")
message = driver.find_element(By.CLASS_NAME, "alert-success").text

print(message)
assert "Success" in message
