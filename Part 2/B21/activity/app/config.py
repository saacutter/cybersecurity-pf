import os
from dotenv import load_dotenv

class Config:
    # Load the environment variables from the .env file
    load_dotenv()
   
    # Set the secret key
    SECRET_KEY = os.getenv('SECRET_KEY') or 'secret-key'

class DeploymentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), "app.db")

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True