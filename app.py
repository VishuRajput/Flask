from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World! Welcome to my Development Server</h1>"

@app.route("/hello_world1")
def hello_world1():
    return "<h2>You dont Know me!</h2>"

@app.route("/hello_world2")
def hello_world2():
    return "<h3>I Am INVISIBLE!!!!!</h3>"

@app.route('/test')
def test():
    a=5+6
    return 'This is my function to run app {}'.format(a)

@app.route('/test1')
def test1():
    data = request.args.get('x')
    return 'this is a data from my url {}'.format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
