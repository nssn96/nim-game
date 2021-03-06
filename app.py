# Name : Surya Narayanan Nadhamuni Suresh
# UTA ID : 1001877873

from flask import Flask, redirect,render_template, request,url_for,flash,jsonify,json
from pusher import pusher



app = Flask(__name__)
app.secret_key = 'random string'





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/player1')
def player1():
    return render_template('player1.html')

@app.route('/player2')
def player2():
    return render_template('player2.html')




@app.route('/name1',methods=['POST','GET'])
def name1():
    global playername1
    global playername2
    if request.method=='POST':

        dic={}
        for key,value in request.form.items():
            if value!='':
                dic[key]=value
                playername1=value
                playername2=''
        
        print(dic)
    return render_template('gameroom.html',data1=playername1,data2=playername2)

@app.route('/name2',methods=['POST','GET'])
def name2():
    if request.method=='POST':

        dic={}
        for key,value in request.form.items():
            if value!='':
                dic[key]=value
                playername2=value

    
        print(dic)

    return render_template('gameroom.html',data1=playername1,data2=playername2)





if __name__ == "__main__":
    app.run()