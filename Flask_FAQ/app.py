from flask import Flask, redirect, url_for,request,render_template, Response
from elastic_api import *

app = Flask(__name__)

#-----------------------ROUTE-----------------------------------
@app.route('/')
def base():
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/entry')
def entry():
    return render_template('entry.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/test')
def test():
    return render_template('entry.html')
#----------------------------------------------------------

#-----------------------ADD-----------------------------------
@app.route('/entry', methods=['POST','GET'])
def add():
    if request.method == 'POST':
        tic = request.form['tic']
        pro = request.form['pro']
        cus = request.form['cus']
        sub = request.form['sub']
        top = request.form['top']
        des = request.form['des']
        sup = request.form['sup']

        return Response(add_data(tic,pro,cus,sub,top,des,sup))
    
def add_data(tic,pro,cus,sub,top,des,sup):
    es = elastic()
    es.connect()
    es.add(tic,pro,cus,sub,top,des,sup)
    return render_template('entry.html')
#--------------------------------------------------------------

#-----------------------UPDATE-----------------------------------

@app.route('/edit', methods=['POST','GET'])
def update():
    if request.method == 'POST':
        tic = request.form['tic']
        pro = request.form['pro']
        cus = request.form['cus']
        sub = request.form['sub']
        top = request.form['top']
        des = request.form['des']
        sup = request.form['sup']

        return Response(update_data(tic,pro,cus,sub,top,des,sup))
    
def update_data(tic,pro,cus,sub,top,des,sup):
    es = elastic()
    es.connect()
    es.update(tic,pro,cus,sub,top,des,sup)
    return render_template('entry.html')

#----------------------------------------------------------

#-----------------------SEARCH-----------------------------------

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == "POST":
        user = request.form['keyword']
        return Response(search_data(user))

@app.route('/search', methods=['POST','GET'])
def check():
    if request.method == 'POST':
        user = request.form['keyword']
        return Response(search_data(user))
    
def search_data(data):
    es = elastic()
    es.connect()
    es.search(data)
    return render_template('search.html')

#----------------------------------------------------------

if __name__ == '__main__':
    app.run()
