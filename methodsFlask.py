from flask import Flask, request

app = Flask(__name__)

@app.route('/api/<path:param>', methods = ['GET', 'POST','PUT','DELETE'])
def index(param):
    if request.method == 'DELETE':
        print(f'Delete: {param}')
    elif request.method == 'GET':
        print(f'Retrieve: {param}')
    elif request.method == 'POST':
        print(f'POST data for {param}')
        for key in request.form:
            print(key + ': ' + request.form[key])

    return f'Hello, {request.method} {param}\n'

if __name__=='__main__':
    app.run()