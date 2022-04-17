# Name : Surya Narayanan Nadhamuni Suresh
# UTA ID : 1001877873

from flask import Flask,render_template, request,url_for,flash



app = Flask(__name__)
app.secret_key = 'random string'








@app.route('/')
def index():
    return render_template('index.html')





if __name__ == "__main__":
    app.run()