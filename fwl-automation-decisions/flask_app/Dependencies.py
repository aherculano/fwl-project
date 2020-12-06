from domain.model.environment import EnvironmentRepository
from domain.model.zone import ZoneRepository
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from infrastructure.flsql.SQLAlchemyBase import SQLAlchemyBase
from infrastructure.flsql.repository import EnvironmentRepositorySQL
from infrastructure.flsql.repository.ZoneRepositorySQL import ZoneRepositorySQL
from injector import Module, singleton


class AppModule(Module):

    def __init__(self, app: Flask, db: SQLAlchemy):
        self.app = app
        self.db = db

    def configure(self, binder):
        base_repo = SQLAlchemyBase(self.db)
        environment_repository = EnvironmentRepositorySQL(base_repo)
        zone_repository = ZoneRepositorySQL(base_repo)
        binder.bind(EnvironmentRepository, to=environment_repository, scope=singleton)
        binder.bind(ZoneRepository, to=zone_repository, scope=singleton)
