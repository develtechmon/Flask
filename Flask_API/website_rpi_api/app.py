from flask import Flask, request, jsonify

app = Flask(__name__)

# API endpoint to receive data
@app.route('/api/data', methods=['POST'])
def receive_data():
    # Receive data from request body
    data = request.get_json()

    # Process data (for example, print it)
    print('Received data:', data)

    # Send response back to client
    response = {'message': 'Data received'}
    return jsonify(response)

if __name__ == '__main__':
    # Run the Flask app on the Raspberry Pi
    app.run(host='192.168.195.190', port=80,threaded=True)