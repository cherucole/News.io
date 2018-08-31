from flask import render_template
from app import app
from .request import get_sources,get_articles,get_category

@app.route('/')
def index():
    '''
    my index page
    :return:
    '''
    sources=  get_sources()
    print(sources)
    message= "Test Dynamic message"
    return render_template('index.html', sources = sources, message=message)

# @app.route('/article/')
@app.route('/articles/<id>')
def articles(id):

    '''
    View  page function that returns the details page and its data
    '''
    name="cherucole"
    articles=get_articles(id)
    # print(articles)
    # title=f'{articles.title}'
    return render_template('articles.html', articles=articles, name=name,name_source=id)

@app.route('/categories/<category>')
def categories(category):

    '''
    View  page function that returns the details page and its data
    '''
    cat="cherucole"
    category=get_category(category)
    print(category)
    # articles=get_articles(id)
    # print(articles)
    # title=f'{articles.title}'
    return render_template('categories.html', category=category,name_source=id)