from flask import Flask, redirect, url_for,request,render_template, Response
import requests
import json

import urllib.request
import urllib.parse

#import httplib2

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
        
        '''
        1st Method in HTML- Enable this if want to send data using url method 
        '''
        # for key, value in data.items():
        #     return Response(update_data(key))
        
        '''
        2nd and 3rd Method in HTML- Enable this if want to send data from html directly.
        Here, open, close and pause parameters were sent from
        a. html form - 2nd method
        b. Javascript - 3rd method
        '''
        return render_template('control.html')

def update_data(key):
    '''
    1st Method
    Work on zerotier connection only for local computer and RPI if the deplyoment of this
    server deploy in this computer not in server -etc pythonanywhere.com
    '''  
    print(key)
    data = key
    #url="http://192.168.195.154:80/api/data"
    url = 'http://10.60.215.170:80/api/data'
    response = requests.post(url, json=data)
    #rpi_relay(key)

    '''
    2nd Method
    Work on zerotier connection only for local computer and RPI if the deplyoment of this
    server deploy in this computer not in server -etc pythonanywhere.com
    '''
    # h = httplib2.Http()
    # data = key
    # headers = {'Content-Type': 'application/json'}
    # url = 'http://10.60.215.170:80/api/data'
    # resp, content = h.request(uri=url, method='POST', body=json.dumps(data), headers=headers)

    '''
    3rd Method
    Work on zerotier connection only for local computer and RPI if the deplyoment of this
    server deploy in this computer not in server -etc pythonanywhere.com
    '''
    # print(key)
    # data = key
    # headers = {'Content-type': 'application/json'}
    # url="http://10.60.215.170:80/api/data"
    # #url="http://192.168.195.154:80/api/data" 
    # response = requests.post(url, data=json.dumps(data), headers=headers)

    return render_template('control.html')   

if __name__ == '__main__':

    # Using PC/Laptop Zerotier IP address at port 80
    #app.run(host='192.168.195.190', port=80, threaded=True)

    # Using 0 address to at port 80 to accept any incoming data in this pipeline
    #app.run(host='0.0.0.0', port=80)

    # Just run
    app.run()
