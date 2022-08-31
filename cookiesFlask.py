from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/cookies/<val>')
def cookies_set(val):
    res = make_response('Hello, Cookies')
    res.set_cookie('my_cookie', val)
    return res

@app.route('/cookies')
def cookies_get():
    return str(request.cookies.get('my_cookie'))

if __name__ == '__main__':
    app.run()