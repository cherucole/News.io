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
@app.route('/articles/<articles_name>')
def articles(articles_name):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('articles.html',name = articles_name)