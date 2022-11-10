'''
Here we pass the value from url "postID and revNo" to the function
http://127.0.0.1:5000/hello/World 

'''
from flask import Flask

app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision number %f' % revNo

if __name__ == '__main__':
    app.run()