from flask import Flask, request, render_template
from helper import flipkart
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def result():
    if request.method=="POST":
        searchData = request.form["search"]
        print(searchData)
        flipkart(searchData)
        return render_template('index.html')
    # return(searchData)


if __name__ =='__main__':
    app.run(debug = True)