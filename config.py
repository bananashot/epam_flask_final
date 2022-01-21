from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()
user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
server = os.environ.get('POSTGRES_SERVER')
port = os.environ.get('POSTGRES_PORT')
database = os.environ.get('POSTGRES_DATABASE')
database_test = os.environ.get('POSTGRES_DATABASE_TEST')
api_key = os.environ.get('API_KEY')
secret_key = os.environ.get('SECRET_KEY')
user_username = os.environ.get('USER_USERNAME')
user_password = os.environ.get('USER_PASSWORD')


class Config(object):
    """
    Base configurations
    """
    DEBUG = True
    SECRET_KEY = secret_key
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{server}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    api_key = api_key


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{server}:{port}/{database}'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """
    SECRET_KEY = os.urandom(32)
    TESTING = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@{server}:{port}/{database}'
