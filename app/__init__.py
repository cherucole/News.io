from flask import Flask
# from config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()


def create_app(config_name):
    bootstrap = Bootstrap()

    # Bootstrap()

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    # Will add the views and forms

    return app
#
# #initializing the application
# app = Flask(__name__,instance_relative_config=True)
#
#
# #Setting up the configuration for testing and production
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')
#
# Bootstrap(app)
#
#
#
# from app import views
# from app import error
