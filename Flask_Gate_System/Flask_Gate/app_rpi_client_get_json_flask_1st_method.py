from flask import Flask, request

app = Flask(__name__)

@app.route('/api/data',  methods=['POST','GET'])
def api():

    '''
    This method works when app.py include following statement. Bear in mind, this method
    will work only using zero tier and local host. 
    
    data = key
    url="http://192.168.195.154:80/api/data"
    response = requests.post(url, json=data)
    '''
    data = request.get_json()
    print(data)
    return 'Data received'

if __name__ == '__main__':
    # Using IP Zerotier IP address at port 80
    #app.run(host='192.168.195.154', port=80)

    # Using 0 address to at port 80 to accept any incoming data in this pipeline
    app.run(host='0.0.0.0', port=80)
    #app.run(host='10.60.215.170', port=80)
    
    # Just run
    #app.run()
