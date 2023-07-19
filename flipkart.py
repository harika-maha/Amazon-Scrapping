from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
options =Options()
options.add_argument("incognito")
driver=webdriver.Chrome('C:\\Users\\vaishali\\Downloads\\chromedriver_win32\\chromedriver.exe',options=options)
driver.get("https://www.flipkart.com/")

time.sleep(5)

search=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
time.sleep(5)
search.send_keys("macbook")
searchbutton=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
time.sleep(5)
searchbutton.submit()
time.sleep(5)
firstelement=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a')
productlink=firstelement.get_attribute('href')
time.sleep(5)
print("hey"+productlink)








