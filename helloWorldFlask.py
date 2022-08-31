from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	print ('Hello, Console!')
	return 'Hello, Web Browser!'

if __name__=='__main__':
	app.run()
