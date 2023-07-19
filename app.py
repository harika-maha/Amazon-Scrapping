from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def result():
    searchData = request.form
    return(searchData)


if __name__ =='__main__':
    app.run(debug = True)