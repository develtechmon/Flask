from flask import Flask, redirect, url_for,request,render_template, Response

app = Flask(__name__)

#-----------ROUTE---------------
@app.route('/')
def base():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/control')
def control():
    print("home here")
    return render_template('control.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    
    # Using PC/Laptop Zerotier IP address at port 80
    #app.run(host='192.168.195.190', port=80, threaded=True)

    # Using 0 address to at port 80 to accept any incoming data in this pipeline
    app.run(host='0.0.0.0', port=80)

    # Just run
    # app.run()
