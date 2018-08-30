from flask import Flask
from .config import DevConfig

#initializing the application
app = Flask(__name__)


#Setting up the configuration for testing and production
app.config.from_object(DevConfig)


from app import views