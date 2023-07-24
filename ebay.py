from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup as bs
import requests as r

options =Options()

# options.add_argument("incognito")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Chrome('C:\\Users\\vaishali\\Downloads\\chromedriver_win32\\chromedriver.exe',options=options)
actions = ActionChains(driver)
driver.get("https://www.ebay.com/")

time.sleep(5)

search=driver.find_element(By.XPATH,'//input[@CLASS="gh-tb ui-autocomplete-input"]')
time.sleep(5)
search.send_keys("macbook")
time.sleep(5)
searchbtn=driver.find_element(By.XPATH,'//*[@id="gh-btn"]').click()
print ("Search button clicked.")
firstelementurl=driver.find_element(By.XPATH,'//*[@id="item2b45ac98b6"]/div/div[2]/a').get_attribute('href')
print(firstelementurl)
time.sleep(15)
# searchbutton=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
# time.sleep(5)
# searchbutton.submit()
# time.sleep(5)
# firstelement=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a')
# productlink=firstelement.get_attribute('href')
# time.sleep(5)
# print("hey"+productlink)

url = firstelementurl

page = r.get(url)

soup = bs(page.content, "html.parser")

divTag = soup.find("div", {"class":"x-price-primary"})
# price = soup.find('span', {"class":"ux-textspans"})
# price = re.findall("$", divTag)


# price = [soup.find('span', {"class":"ux-textspans"}) for div in soup.find('div', {"class":"x-price-primary"})]

divStr = str(divTag)
divArray = divStr.split()
print(divArray)

val=divArray[4][:4]
print(val[1:])






