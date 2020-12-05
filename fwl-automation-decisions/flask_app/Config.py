import os

from dotenv import load_dotenv


class BaseConfig(object):
    load_dotenv()


class DevelopmentConfig(BaseConfig):
    FLASK_DEBUG: bool = True
    FLASK_ENV: str = "development"
    SQLALCHEMY_DATABASE_URI: str = os.getenv("SQLALCHEMY_DATABASE_URI") or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS: str = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS") or False


class TestConfig(object):
    FLASK_DEBUG = True
    FLASK_ENV = "test"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
