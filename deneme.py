from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

driver.get("https://www.google.com/")

input= driver.find_element(By.NAME,"q")
input.send_keys("deneme")
sleep(3)

searchBtn= driver.find_element(By.NAME,"btnK")
searchBtn.click()
