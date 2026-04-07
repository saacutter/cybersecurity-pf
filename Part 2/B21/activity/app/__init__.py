from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'main.login' # This sets the page that should be rendered when there is a page that requires a log in to view

def create_application(config):
    # Initialise the Flask server
    application = Flask(__name__)
    application.config.from_object(config)

    # Configure the routes from the blueprint
    from app.blueprints import blueprint
    application.register_blueprint(blueprint)

    # Initialise the components of the application
    db.init_app(application)
    login.init_app(application)

    return application