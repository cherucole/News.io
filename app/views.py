from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    my index page
    :return:
    '''
    my_message= "Test Dynamic message"
    return render_template('index.html', message=my_message)

# @app.route('/article/')