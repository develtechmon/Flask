from flask import Flask, redirect, url_for,request,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['data']
        return render_template('index.html',name=user)

if __name__ == '__main__':
    app.run(debug=True)