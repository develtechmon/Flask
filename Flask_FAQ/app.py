from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/entry')
def entry():
    return render_template('entry.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()
