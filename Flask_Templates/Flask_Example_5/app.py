from flask import Flask, render_template

app = Flask(__name__)

@app.route('/result')
def result():
    x = "Flask Endpoint Check"
    return render_template('index.html',result=x)

if __name__ == '__main__':
    app.run(debug=True)