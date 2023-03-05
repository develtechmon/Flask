from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.form['data']
    # process the data here
    return 'OK'

if __name__ == '__main__':
    '''
    This IP address is referring to Rpi IP address
    '''
    app.run(host='192.168.195.154', port=80)
    #app.run(host='0.0.0.0', port=80)
