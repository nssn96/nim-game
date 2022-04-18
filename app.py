# Name : Surya Narayanan Nadhamuni Suresh
# UTA ID : 1001877873

from flask import Flask, redirect,render_template, request,url_for,flash,jsonify,json
from pusher import pusher
from flask_socketio import SocketIO, send,emit



app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = 'random string'


@socketio.on('my event')
def handle_my_custom_event(data):
    print('received data: ' + str(data))

@socketio.on('my event')
def handle_my_custom_event(data):
    emit('my response', data,broadcast=True)





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/player1')
def player1():
    return render_template('player1.html')

@app.route('/player2')
def player2():
    return render_template('player2.html')

@app.route('/gameroom')
def gameroom():
    return render_template('gameroom.html')




@app.route('/name1',methods=['POST','GET'])
def name1():
    if request.method=='POST':

        dic={}
        for key,value in request.form.items():
            if value!='':
                dic[key]=value
        
        print(dic)
    return render_template('gameroom.html',data1=dic)

@app.route('/name2',methods=['POST','GET'])
def name2():
    if request.method=='POST':

        dic={}
        for key,value in request.form.items():
            if value!='':
                dic[key]=value
    
        print(dic)

    return render_template('gameroom.html',data2=dic)

@app.route('/playdetails',methods=['POST','GET'])
def playdetails():
    if request.method=='POST':

        dic={}
        for key,value in request.form.items():
            if value!='':
                dic[key]=value
        #To change the pile stone count to integer
        for k in dic:
            if k!='first':
                dic[k]=int(dic[k])
        

    return render_template('gameroom.html',details=dic)





if __name__ == "__main__":
    #app.run()
    socketio.run(app)