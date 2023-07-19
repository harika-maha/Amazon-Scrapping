from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
options =Options()
options.add_argument("incognito")
driver=webdriver.Chrome('C:\\Users\\vaishali\\Downloads\\chromedriver_win32\\chromedriver.exe',options=options)
driver.get("https://www.amazon.com/")

# search_box=driver.find_element(By.XPATH,'//textarea[@CLASS="gLFyf"]')


# search_box.send_keys("amazon.com")
# time.sleep(25)
# search_box.send_keys(Keys.ENTER)
# link=driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a')
# url=link.get_attribute('href')
# driver.get(url)
# search_btn=driver.find_element(By.XPATH,'//link[@CLASS="Tg7LZd search_button_suggest"]')
# search_btn.submit()

# driver.get("https://www.amazon.com/")
time.sleep(5)
search_query=driver.find_element(By.XPATH,'//input[@ID="twotabsearchtextbox"]')
time.sleep(5)
search_query.send_keys("macbook")
time.sleep(6)
search_btn =driver.find_element(By.XPATH,'//input[@ID="nav-search-submit-button"]')
search_btn.submit()
time.sleep(4)
urltag=driver.find_element(By.XPATH,'//a[@CLASS="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
time.sleep(4)
actualurl=urltag.get_attribute('href')
print("hey"+actualurl)
time.sleep(2)

