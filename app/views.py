from flask import render_template
from app import app
from .request import get_sources

@app.route('/')
def index():
    '''
    my index page
    :return:
    '''
    sources=  get_sources()
    print(sources)
    # my_message= "Test Dynamic message"
    return render_template('index.html', sources = sources)

# @app.route('/article/')