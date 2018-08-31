from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap


#initializing the application
app = Flask(__name__,instance_relative_config=True)


#Setting up the configuration for testing and production
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

Bootstrap(app)



from app import views
from app import error
