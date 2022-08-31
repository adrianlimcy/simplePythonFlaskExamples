# Ginger

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title='Top 100 eBooks'
    alias=None
    ebooks = [
        {
            'author': 'Jane Austen',
            'book': 'Pride & Prejudice',
            'year': 1813
        },
        {
            'author': 'Joseph Conrad',
            'book': 'Heart of Darkness',
            'year': 1899
        },
        {
            'author': 'Oscar Wilde',
            'book': 'The Importance of Being Earnest: A Trival Comedy for Serious People',
            'year': 1895
        }
    ]
    return render_template('index.html', title=title, alias=alias, ebooks=ebooks)

if __name__=='__main__':
    app.run()