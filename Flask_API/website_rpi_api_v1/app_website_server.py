from flask import Flask, redirect, url_for,request,render_template, Response

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('index.html')
 
if __name__ == '__main__':
    '''
    This ip address referring to this pc ip address
    '''
    app.run(host='192.168.195.190', port=80,threaded=True)