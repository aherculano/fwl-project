from flask_sqlalchemy import SQLAlchemy
from .EnvironmentModel import EnvironmentModel
from .ZoneModel import ZoneModel
from .FirewallModel import FirewallModel


def flask_sqlalchemy_mappings(db: SQLAlchemy):
    metadata = db.metadata

    environment_mapping = db.Table('datacenter_environment',
                                   metadata,
                                   db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                                   db.Column('name', db.String(128), unique=True))

    zone_mapping = db.Table('zone',
                            metadata,
                            db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                            db.Column('name', db.String(128), unique=True),
                            db.Column('env_id', db.Integer, db.ForeignKey('datacenter_environment.id')))

    firewall_mapping = db.Table('firewall',
                                metadata,
                                db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                                db.Column('uuid', db.String(128), unique=True),
                                db.Column('name', db.String(128)),
                                db.Column('access_layer', db.String(128)))

    db.mapper(EnvironmentModel, environment_mapping)
    db.mapper(ZoneModel, zone_mapping, properties={
        "environment": db.relationship(EnvironmentModel,
                                            primaryjoin=zone_mapping.c.env_id == environment_mapping.c.id,
                                            backref='zone')
    })
    db.mapper(FirewallModel, firewall_mapping)
