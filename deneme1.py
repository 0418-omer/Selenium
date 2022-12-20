from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("./chtomedriver.exe")
driver = webdriver.Chrome(service=service)


driver.get("https://www.apple.com/tr/")
link = driver.current_url
baslik =driver.title
print("sayfa baslığı"+baslik)
if "apple.com" in link:
    print("Doğru apple sayfası:" +link)


driver.get("https://www.etsy.com/")
link = driver.current_url
baslik =driver.title
print("sayfa baslığı" + baslik)
if "etsy.com" in link:
    print("doğru etys sayfası"+ link)
driver.back()
baslik = driver.title
if "apple" in baslik:
    print("tebrikler apple sayfasına döndün")

    

