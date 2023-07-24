from bs4 import BeautifulSoup as bs
import requests as r
import regex as re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os



PATH=os.environ.get('PATH')

def flipkart(searchData):
    # path = "/usr/local/bin/chromedriver.exe"
    options =Options()
    options.add_argument("--headless")
    options.add_argument("incognito")
    driver = webdriver.Chrome('C:\\Users\\vaishali\\Downloads\\chromedriver_win32\\chromedriver.exe',options=options)

    driver.get("https://www.flipkart.com/")

    time.sleep(6)

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

def ebay(searchData):
    options =Options()

    # options.add_argument("incognito")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver=webdriver.Chrome(options=options)
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

    url = firstelementurl

    page = r.get(url)

    soup = bs(page.content, "html.parser")

    divTag = soup.find("div", {"class":"x-price-primary"})
    # price = soup.find('span', {"class":"ux-textspans"})
    # price = re.findall("$", divTag)


    # price = [soup.find('span', {"class":"ux-textspans"}) for div in soup.find('div', {"class":"x-price-primary"})]

    divStr = str(divTag)
    divArray = divStr.split()

    # divArray[5]

    print(divArray[4][:4]*86)
