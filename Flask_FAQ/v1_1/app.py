from flask import Flask, redirect, url_for,request,render_template, Response, jsonify,session
from elastic_api import *
from forms import FilterForm

app = Flask(__name__)
app.secret_key = 'hello'

#-----------------------ROUTE-----------------------------------
@app.route('/')
def base():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/search')
def search():
    es = elastic()    
    es.connect()
    res = es.search('xs018')
    x = res['hits']['hits']
    
    if x !=None:
        return render_template(
            'search.html',
            res=res['hits']['hits'],
            all = len(x)
            )
    else:
         return render_template(
            'search.html',
            res=res['hits']['hits'],
            all = 0
            )

@app.route('/entry')
def entry():
    return render_template('edit.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

# @app.route('/display')
# def display():
#     return render_template('display.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/open', methods=['POST','GET'])
def open():
    data = request.get_json()

    '''
    Method to send data to new page to open new tab
    ticket = data['tickets']
    process = data['process']
    subject = data['subject']
    '''
    session['data'] = data

    return jsonify({'redirect_url': url_for('display')})

    #output = request.args.get('subject')
    #return render_template('open.html',output=subject)

@app.route('/display')
def display():
    data = session.get('data')
    ticket   = data['tickets']
    process  = data['process']
    subject  = data['subject']
    question = data['question']
    topic    = data['topic']
    answer   = data['answer']
    print(subject.strip())
    return render_template('display.html',TICKET=ticket.strip(),PROCESS=process.strip(),SUBJECT=subject.strip(),QUESTION=question.strip(),TOPIC=topic.strip(),ANSWER=answer.strip()) 

#----------------------------------------------------------

#-----------------------SEARCH-----------------------------------
@app.route('/search', methods=['POST','GET']) # type: ignore
def check():
    if request.method == 'POST':
        user = request.form['keyword']        
        return Response(search_data(user))
    
def search_data(data):
    es = elastic()
    es.connect()
    #process = request.args.get('Process', default='xh018')

    res = es.search(data)
    
    x = res['hits']['hits']

    if x != None:
        return render_template(
        'search.html',
        res=res['hits']['hits'],
        all = len(x)
        )

    else:
        return render_template(
        'search.html',
        res=res['hits']['hits'],
        all = 0
        )
   
    
if __name__ == '__main__':
    app.run()
