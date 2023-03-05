from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.form['data']
    # process the data here
    return 'OK'

if __name__ == '__main__':
    app.run(host='192.168.195.190', port=80,threaded=True)