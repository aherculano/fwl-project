from domain.model.environment import EnvironmentRepository
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from infrastructure.flsql.SQLAlchemyBase import SQLAlchemyBase
from infrastructure.flsql.repository import EnvironmentRepositorySQL
from injector import Module, singleton


class AppModule(Module):

    def __init__(self, app: Flask, db: SQLAlchemy):
        self.app = app
        self.db = db

    def configure(self, binder):
        base_repo = SQLAlchemyBase(self.db)
        environment_repository = EnvironmentRepositorySQL(base_repo)
        binder.bind(EnvironmentRepository, to=environment_repository, scope=singleton)

