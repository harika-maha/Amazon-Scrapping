from flask import Flask, request, render_template
from helper import flipkart
from helper import ebay
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

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def result():
    if request.method=="POST":
        searchData = request.form["search"]
        print(searchData)
        flip=flipkart(searchData)
        flipkartprice = flip['fprice']
        flipkarturl = flip['furl']
        eb = ebay(searchData)
        ebayprice = (float(eb['eprice'])*86)
        ebayurl = eb['eurl']
        print(flipkartprice)
        print(ebayprice)

        result={
            "productName":searchData,
            "flipkartPrice": flipkartprice
        }

        x= new_collection.insert_one(result)
        # amazon(searchData)
        # ebayprice=ebay(searchData)
        query = {"productName":searchData}
        new_field_name = "ebayPrice"
        new_field_value = ebayprice

        # The update operation using $set to add a new field to the document
        update_query = {"$set": {new_field_name: new_field_value}}

        # Use update_one to update a single document that matches the query condition
        new_collection.update_one(query, update_query)
        print("done")


        return render_template('comparison.html', flipkartprice=flipkartprice, ebayprice=ebayprice, flipkarturl=flipkarturl, ebayurl=ebayurl)
    # return(searchData)

if __name__ =='__main__':
    app.run(debug = True)