from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():

    '''
    This method works when control.html include following statement
     <form action="http://192.168.195.154:80/api" method="POST">
    '''

    '''
    To extract the dictionary value
    '''
    #data = request.form['open']
    
    '''
    To compile the dictionary of form from Webserver into one dicitonary
    '''
    data = request.form
    
    '''
    To extract key and value of dictionary
    '''
    for key, value in data.items():
        print(value)
    
    return 'OK'

if __name__ == '__main__':
    # Using IP Zerotier IP address at port 80
    #app.run(host='192.168.195.154', port=80)

    # Using 0 address to at port 80 to accept any incoming data in this pipeline
    #app.run(host='0.0.0.0', port=80)

    # Office
    #app.run(host='10.60.215.170', port=80)

    # Visitor
    app.run(host='10.60.129.54',port=80)

    # Just run
    #app.run()
