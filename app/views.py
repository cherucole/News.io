from flask import render_template
from app import app
from .request import get_sources,get_articles

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
@app.route('/articles/<id>')
def articles(id):

    '''
    View  page function that returns the details page and its data
    '''
    name="cherucole"
    articles=get_articles(id)
    print(articles)
    # title=f'{articles.title}'
    return render_template('articles.html', articles=articles, name=name)