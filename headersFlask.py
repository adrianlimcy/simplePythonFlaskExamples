from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    print(request.headers)
    return 'Hello, {}!/n'.format(request.headers.get("User-Agent"))

if __name__=="__main__":
    app.run()