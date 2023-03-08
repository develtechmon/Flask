from flask import Flask, redirect, url_for,request,render_template, Response,session
from flask_cors import CORS

app = Flask(__name__)
#CORS(app)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app, supports_credentials=True)

@app.route('/')
def base():
    return render_template('index.html')
 
if __name__ == '__main__':
    '''
    This ip address referring to this pc ip address
    '''
    #app.run(host='10.60.215.170', port=80)
    app.run()