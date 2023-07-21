from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from bs4 import BeautifulSoup as bs
import requests as r

load_dotenv()


PORT            = os.environ.get('PORT')
MONGO_URI       = os.environ.get('MONGO_URI')
DB_NAME         = os.environ.get('DB_NAME')

# creating a MongoClient object
client = MongoClient(MONGO_URI)

# accessing the database
database = client[DB_NAME]
collection_name = 'productPrice'
new_collection = database[collection_name]


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
url = productlink

page = r.get(url)

soup = bs(page.content, "html.parser")

price = soup.find("div", {"class":"_30jeq3 _16Jk6d"}).text

print(price)


result={
    "productName":"macbook",
    "flipkartPrice": price
}

x= new_collection.insert_one(result)
print(x)





