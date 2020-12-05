from flask import Flask
from flask_injector import FlaskInjector
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from infrastructure.flsql.model import flask_sqlalchemy_mappings
from injector import Injector

from .controller.Endpoints import api_bp
from .Dependencies import AppModule
from .Config import TestConfig


def create_app(config=TestConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    db = SQLAlchemy(app)
    flask_sqlalchemy_mappings(db)
    Migrate(app, db)
    app.register_blueprint(api_bp)
    injector = Injector([AppModule(app, db)])
    FlaskInjector(app=app, injector=injector)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
