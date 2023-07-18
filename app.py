from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome('C:\\Users\\vaishali\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get("https://www.amazon.com/")



search_query=driver.find_element(By.XPATH,'//input[@ID="twotabsearchtextbox"]')
search_query.send_keys("mac book")
# #locate Google Search button by _xpath code 3
search_btn =driver.find_element(By.XPATH,'//input[@ID="nav-search-submit-button"]')
# # use submit() to mimic enter key code 4
search_btn.submit()
urltag=driver.find_element(By.XPATH,'//a[@CLASS="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
actualurl=urltag.get_attribute('href')
print(actualurl)

# driver.get(actualurl)
# time.sleep(5)#wait for page load complete