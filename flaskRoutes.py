from crypt import methods
from re import T
from webbrowser import get
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/method', methods=['GET', 'POST'])
def method():
    return request.method

@app.route('/info/<data>')
def info(data):
    return str(data)

@app.route('/double/<float:val>')
@app.route('/double/<int:val>')
def double(val):
    return str(2 * val)

if __name__ == '__main__':
    app.run()