from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# vikipediadan yazı okumak
driver = webdriver.Chrome()
driver.get("https://tr.wikipedia.org/wiki/T%C3%BCrk%C3%A7e_Vikipedi")
driver.maximize_window()
seckin_madde_alanı = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/main/div[2]/div[3]/div[1]/p[6]")
sleep(3)
# vikipediadan yazı okumak
seckin_madde_alanı = seckin_madde_alanı.text
# vikipediadan indis ile alan getirmek 
seckin_madde_alanı=seckin_madde_alanı.split(",")[0]
print(seckin_madde_alanı)
sleep(3)
