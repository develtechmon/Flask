from flask import Flask, redirect, url_for,request,render_template, Response, jsonify,session
from elastic_api import *
from forms import FilterForm

app = Flask(__name__)
app.secret_key = 'hello'
#-----------------------ROUTE-----------------------------------
@app.route('/', methods=['POST','GET'])
def base():
    #return render_template('search.html')
    #return redirect(url_for(
    #    'search',
        #process='xt018'
    #))
    es = elastic()
    
    # NOTE: Get the  filter values from the form
    process = request.args.get('Process', default='xs018')
    
    es.connect()
    res = es.search(process)
    x = res['hits']['hits']
    
    return render_template(
        'search.html',
        res=res['hits']['hits'],
        all = len(x)
    )

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

@app.route('/search')
def search():
    return render_template('search.html',all=0)

@app.route('/entry')
def entry():
    return render_template('display.html')

'''
    es = elastic()
    
    # NOTE: Get the  filter values from the form
    process = request.args.get('Process', default='xt018')
    
    es.connect()
    res = es.search(process)
    x = res['hits']['hits']
    
    return render_template(
        'search.html',
        res=res['hits']['hits'],
        all = len(x)
    )
'''
    
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
    print(x)
    
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
                
@app.route('/entry')
def edit():
    return render_template('entry.html')
 
'''

@app.route('/search', methods=['GET','POST'])
def search():
    #filter_form = FilterForm()
    es = elastic()
    # NOTE: Redirect on form submit with selected values
    #if request.method == 'POST' and 'apply_submit' in request.form:
    #    return redirect(url_for(
    #        'search',
            #ticket = filter_form.ticket.data,
    #        process = filter_form.process.data
            #question = filter_form.question.data,
            #topic = filter_form.topic.data,
            #answer = filter_form.answer.data
        #))
        
    # NOTE: Get the  filter values from the form
    process = request.args.get('Process', default='xt018')
    
    es.connect()
    res = es.search(process)
    x = res['hits']['hits']
    
    #print(len(x))
    
    # all = []
    # for hit in x:
    #     all.append(hit)
    # print(len(all))
    
    #print(x)
    #print(x[0]['_source']['Process'])
    
    value = res['hits']['total']['value']
    
    return render_template(
        'search.html',
        res=res['hits']['hits'],
        all = len(x)
    )
    
'''
            
#-----------------------SEARCH-----------------------------------
# @app.route("/", methods=['GET'])
# def base():
#     return redirect(url_for(
#         'search',
#         ticket = 111111,
#         process = "XH018",
#         question = "Do XT018 support RISCV ?",
#         topic = "RISCV Processor",
#         answer = "It does support but low power"
#     ))

if __name__ == '__main__':
    app.run()