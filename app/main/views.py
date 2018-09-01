import datetime as datetime
from flask import render_template
from . import main
from ..request import get_sources,get_articles,get_category
from ..models import Articles,Sources


@main.route('/')
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
@main.route('/articles/<id>')
def articles(id):

    '''
    View  page function that returns the details page and its data
    '''
    name="cherucole"
    articles=get_articles(id)
    # print(articles)
    # title=f'{articles.title}'
    return render_template('articles.html', articles=articles, name=name,name_source=id)

@main.route('/categories/<category_name>')
def categories(category_name):

    '''
    View  page function that returns the details page and its data
    '''
    cat="cherucole"
    category=get_category(category_name)
    print(category_name)
    category_name1=category_name
    # articles=get_articles(id)
    # print(articles)
    # title=f'{articles.title}'
    return render_template('categories.html', category=category,name_source=id,category_name1=category_name1)

# @main.template_filter('strftime')
# def _jinja2_filter_datetime(date, fmt=None):
#     date = dateutil.parser.parse(date)
#     native = date.replace(tzinfo=None)
#     format='%b %d, %Y'
#     return native.strftime(format)