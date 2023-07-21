from bs4 import BeautifulSoup as bs
import requests as r

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def flipkart(searchData):
    # path = "/usr/local/bin/chromedriver.exe"
    options =Options()
    options.add_argument("--headless")
    options.add_argument("incognito")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.flipkart.com/")

    time.sleep(5)

    search=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
    time.sleep(8)
    search.send_keys(searchData)
    searchbutton=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
    time.sleep(5)
    searchbutton.submit()
    time.sleep(5)
    firstelement=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a')
    productlink=firstelement.get_attribute('href')
    time.sleep(5)
    # print("hey  ---- "+productlink)



    url = productlink

    page = r.get(url)

    soup = bs(page.content, "html.parser")

    price = soup.find("div", {"class":"_30jeq3 _16Jk6d"}).text

    print(price)

# flipkart("macbook")