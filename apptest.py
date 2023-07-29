# a test for multiprocessing

from bs4 import BeautifulSoup as bs
import requests as r
# import regex as re
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
from flask import Flask, request, render_template
# from helper import flipkart
# from helper import ebay
import os
from dotenv import load_dotenv
from pymongo import MongoClient

app = Flask(__name__)

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



# PATH=os.environ.get('PATH')

def flipkart(result_queue,searchData):
    # path = "/usr/local/bin/chromedriver.exe"
    options =Options()
    options.add_argument("--headless")
    options.add_argument("incognito")
    driver = webdriver.Chrome('C:\\Users\\vaishali\\Downloads\\chromedriver_win32\\chromedriver.exe',options=options)

    driver.get("https://www.flipkart.com/")

    time.sleep(5)

    search=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
    time.sleep(5)
    search.send_keys(searchData)
    searchbutton=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
    time.sleep(5)
    searchbutton.submit()
    time.sleep(5)
    firstelement=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a')
    productlink=firstelement.get_attribute('href')
    time.sleep(3)
    print("hey  ---- "+productlink)



    url = productlink

    page = r.get(url)

    soup = bs(page.content, "html.parser")

    flipkartprice = soup.find("div", {"class":"_30jeq3 _16Jk6d"}).text
    flipkartprice=flipkartprice.replace(",","")
    flipkarttitle = soup.find("span", {"class":"B_NuCI"}).text

    # return {'fprice':flipkartprice[1:], 'furl': url, 'ftitle': flipkarttitle}
    result_queue.put((flipkartprice[1:]))


def ebay(result_queue,searchData):
    options =Options()

    options.add_argument("incognito")
    options.add_argument("--headless")
    # options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver=webdriver.Chrome('C:\\Users\\vaishali\\Downloads\\chromedriver_win32\\chromedriver.exe',options=options)
    driver.get("https://www.ebay.com/")

    time.sleep(3)

    search=driver.find_element(By.XPATH,'//input[@CLASS="gh-tb ui-autocomplete-input"]')
    time.sleep(5)
    search.send_keys(searchData)
    time.sleep(5)
    searchbtn=driver.find_element(By.XPATH,'//*[@id="gh-btn"]').click()
    print ("Search button clicked.")
    time.sleep(5)
    # firstelementurl=driver.find_element(By.XPATH,'//*[@id="item2b45ac98b6"]/div/div[2]/a').get_attribute('href')
    firstelementurl=driver.find_elements(By.XPATH,'//a[@class="s-item__link"]')[1].get_attribute('href')
    # //*[@id="item5993e959d1"]/div/div[2]/a
    print(firstelementurl)
    time.sleep(3)

    url = firstelementurl

    page = r.get(url)

    soup = bs(page.content, "html.parser")

    divTag = soup.find("div", {"class":"x-price-primary"})
    # price = soup.find('span', {"class":"ux-textspans"})
    # price = re.findall("$", divTag)
    ebaytitle = soup.find("div",{"class":"vim x-item-title"}).find("span", {"class":"ux-textspans ux-textspans--BOLD"}).text

    # price = [soup.find('span', {"class":"ux-textspans"}) for div in soup.find('div', {"class":"x-price-primary"})]

    divStr = str(divTag)
    divArray = divStr.split()
    print(ebaytitle)

    # print(divArray[5])
    val=divArray[4][:4]

    # print(divArray[4][:4]*86)
    # return{'eprice':val[1:], 'eurl':url, 'etitle':ebaytitle}
    result_queue.put((val[1:]))




@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def result():
    if request.method=="POST":
        searchData = request.form["search"]
        print(searchData)
        result_queue=multiprocessing.Queue()
        processA=multiprocessing.Process(target=flipkart,args=(result_queue,searchData))
        processB=multiprocessing.Process(target=ebay,args=(result_queue,searchData))

        processA.start()
        processB.start()

        processA.join()
        processB.join()

        results=[]
        while not result_queue.empty():
            results.append(result_queue.get())
        print(results)

        return render_template('index.html')







        # flip=flipkart(searchData)
        # flipkartprice = flip['fprice']
        # flipkarturl = flip['furl']
        # flipkarttitle = flip['ftitle']
        # eb = ebay(searchData)
        # ebayprice = (float(eb['eprice'])*86)
        # ebayurl = eb['eurl']
        # ebaytitle = eb['etitle']
        # print(flipkartprice)
        # print(ebayprice)

        # result={
        #     "productName":searchData,
        #     "flipkartPrice": flipkartprice
        # }

        # x= new_collection.insert_one(result)
        # # amazon(searchData)
        # # ebayprice=ebay(searchData)
        # query = {"productName":searchData}
        # new_field_name = "ebayPrice"
        # new_field_value = ebayprice

        # # The update operation using $set to add a new field to the document
        # update_query = {"$set": {new_field_name: new_field_value}}

        # # Use update_one to update a single document that matches the query condition
        # new_collection.update_one(query, update_query)
        # print("done")



    # return(searchData)

if __name__ =='__main__':
    app.run(debug = True)