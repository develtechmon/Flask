from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.form['open']
    # process the data here
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
