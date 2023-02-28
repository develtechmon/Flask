from flask import Flask, redirect, url_for,request,render_template, Response
#from rpi_relay import *

app = Flask(__name__)

#-----------ROUTE---------------
@app.route('/')
def base():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/control')
def control():
    return render_template('control.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/about')
def about():
    return render_template('about.html')

#------------CONTROL-------------------
@app.route('/control', methods=['POST','GET'])
def manager():
    if request.method == 'POST':
        data = request.form
        
        for key, value in data.items():
            return Response(update_data(key))

def update_data(key):
  
    # for key,value in data.items():
    #     print(key)
    
    print(key)
    #rpi_relay(key)

    return render_template('control.html')   

if __name__ == '__main__':
    #app.run(host='192.168.195.230', port=80, threaded=True)
    app.run()