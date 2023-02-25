from flask import Flask, redirect, url_for,request,render_template, Response
from rpi_relay import *
app = Flask(__name__)

#-----------ROUTE---------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control')
def control():
    return render_template('control.html')

#------------CONTROL-------------------
@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        data = request.form
        
        for key, value in data.items():
            return Response(update_data(key))

def update_data(key):
    #es = elastic()
    #es.connect()
    #es.update(tic,pro,cus,sub,top,des,sup)
    # for key,value in data.items():
    #     print(key)
    
    print(key)
    rpi_relay(key)

    return render_template('index.html')   

if __name__ == '__main__':
    app.run()