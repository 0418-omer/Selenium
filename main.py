from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

driver.get("https://www.kodlama.io/")
driver.maximize_window() #ekranın tam boyut
sleep(3)
loginBtn = driver.find_element(By.XPATH,"//*[@id='navbar']/div/div/div/ul/li[3]/a")
loginBtnText = loginBtn.text

if loginBtnText == "Giriş Yap":
    print("Test başarılı 😎")
else:
    print("Test Başarısız ❌")

loginBtn.click()