class Config:
    '''
    General configuration parent class
    '''
    # pass
    SOURCE_NEWS_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True