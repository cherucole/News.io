from flask import Flask
from .config import DevConfig

#initializing the application
app = Flask(__name__,instance_relative_config=True)


#Setting up the configuration for testing and production
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views