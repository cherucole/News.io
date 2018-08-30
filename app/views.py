from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    my index page
    :return:
    '''
    return render_template('index.html')