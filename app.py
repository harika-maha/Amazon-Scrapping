from flask import Flask, request, render_template,current_app, g as app_ctx
from helper import flipkart
from helper import ebay
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import multiprocessing
import time

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

@app.before_request
def logging_before():
    # Store the start time for the request
    app_ctx.start_time = time.perf_counter()


@app.after_request
def logging_after(response):
    # Get total time in milliseconds
    total_time = time.perf_counter() - app_ctx.start_time
    time_in_ms = int(total_time * 1000)
    # Log the time taken for the endpoint
    current_app.logger.info('%s ms %s %s %s', time_in_ms, request.method, request.path, dict(request.args))
    return response

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def result():
    if request.method=="POST":
        searchData = request.form["search"]
        print(searchData)
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


        # flip=flipkart(searchData)
        flipkartprice = results[0][0]
        flipkarturl = results[0][1]
        flipkarttitle = results[0][2]
        # eb = ebay(searchData)
        ebayprice = (float(results[1][0])*86)
        ebayurl = results[1][1]
        ebaytitle = results[1][2]
        # print(flipkartprice)
        print(ebayprice)

        result={
            "productName":searchData,
            "flipkartPrice": flipkartprice,
            "ebayPrice":ebayprice
        }

        x= new_collection.insert_one(result)
        # amazon(searchData)
        # ebayprice=ebay(searchData)
        # query = {"productName":searchData}
        # new_field_name = "ebayPrice"
        # new_field_value = ebayprice

        # # The update operation using $set to add a new field to the document
        # update_query = {"$set": {new_field_name: new_field_value}}

        # # Use update_one to update a single document that matches the query condition
        # new_collection.update_one(query, update_query)
        print("done")


        return render_template('comparison.html', flipkartprice=flipkartprice, ebayprice=ebayprice, flipkarturl=flipkarturl, ebayurl=ebayurl, searchData=searchData, flipkarttitle=flipkarttitle, ebaytitle=ebaytitle)
    # return(searchData)

if __name__ =='__main__':
    app.run(host="0.0.0.0", port=5000)