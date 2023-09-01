import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
# click on the column header
driver.find_element(By.XPATH,"//span[normalize-space()='Veg/fruit name']").click()

# collect all  veggie Names --> BrowserSortedVeggielist
veggiesWebelements=driver.find_elements(By.XPATH,"//tr/td[1]")
BrowserSortedVeggielist = []
for veggie in veggiesWebelements:
    BrowserSortedVeggielist.append(veggie.text)
print(BrowserSortedVeggielist)
orginalVeggieslist=BrowserSortedVeggielist.copy()


# SOrt this BrowserSortedVeggielist => newSortedList
BrowserSortedVeggielist.sort()
# BrowserSortedVeggielist == newSortedList

assert  BrowserSortedVeggielist == orginalVeggieslist
print(BrowserSortedVeggielist)
