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
        flipkartprice=flipkart(searchData)

        result={
            "productName":searchData,
            "flipkartPrice": flipkartprice
        }

        x= new_collection.insert_one(result)
        # amazon(searchData)
        ebay(searchData)


        return render_template('index.html')
    # return(searchData)


if __name__ =='__main__':
    app.run(debug = True)