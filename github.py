from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://github.com/")
# giriş yapma
driver.maximize_window()
sleep(3)
loginBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a")
loginBtnText = loginBtn.text
loginBtn.click()
sleep(3)

input= driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/input[2]")
input.send_keys("adiguzelomerrrr@gmail.com")
input= driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[1]")
input.send_keys("24517113206.Om")

sleep(3)
# giriş butonu tıklama
SignInBtn = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[11]")
SignInBtn.click()

sleep(3)
# yeni proje oluşturma 
newR = driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div/aside/div/loading-context/div/div[1]/div/h2/a")
newR.click()


sleep(3)

# proje başlığı girme
title= driver.find_element(By.ID,"repository_name")
title.send_keys("github")

sleep(3)
# description alanı doldurma 
desc= driver.find_element(By.ID,"repository_description")
desc.send_keys("deneme amaçlı proje")
driver.save_screenshot(str(date.today()) + '(2).png')

sleep(4)
# public-private seçme
public=driver.find_element(By.ID,"repository_visibility_private")
public.click()

sleep(4)
# projeyi create etme
create =driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/main/div/form/div[5]/button").click()
create.screenshot("abc.png")


input()







