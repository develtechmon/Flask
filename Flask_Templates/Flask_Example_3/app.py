from flask import Flask, redirect, url_for,request,render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
    return Response('welcome %s' % name)
    
@app.route('/data')
def data():
    return redirect(url_for('success',name="World"))

if __name__ == '__main__':
   app.run(debug = True)