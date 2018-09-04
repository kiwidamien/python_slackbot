import os
from flask import Flask, request, make_response, render_template

app = Flask('HiBot')

@app.route('/')
def homepage():
    return 'Hello world'

if __name__ == '__main__':
    app.run()
