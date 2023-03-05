from flask import Flask, request

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    print(data)
    return 'Data received'

if __name__ == '__main__':
    app.run(host='192.168.195.154', port=80)
