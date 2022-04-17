# Name : Surya Narayanan Nadhamuni Suresh
# UTA ID : 1001877873

from flask import Flask,render_template, request,url_for,flash



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
    
        print(dic)

    return render_template('gameroom.html')





if __name__ == "__main__":
    app.run()