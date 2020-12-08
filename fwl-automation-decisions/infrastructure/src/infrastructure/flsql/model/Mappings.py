from flask_sqlalchemy import SQLAlchemy
from .EnvironmentModel import EnvironmentModel
from .ZoneModel import ZoneModel
from .FirewallModel import FirewallModel
from .AllowedPortModel import AllowedPortModel
from .ZoneConnectionModel import ZoneConnectionModel


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

    zone_connection_mapping = db.Table('zone_connection',
                                       metadata,
                                       db.Column('id', db.Integer, primary_key=True),
                                       db.Column('source_id', db.Integer, db.ForeignKey('zone.id')),
                                       db.Column('destination_id', db.Integer, db.ForeignKey('zone.id')),
                                       db.Column('firewall_id', db.Integer, db.ForeignKey('firewall.id')),
                                       db.Column('criticality', db.Integer),
                                       db.Column('uuid', db.String(128), index=True, unique=True),
                                       db.CheckConstraint('source_id != destination_id'))

    allowed_ports_mapping = db.Table('allowed_ports',
                                     metadata,
                                     db.Column('id', db.Integer, primary_key=True, autoincrement=True),
                                     db.Column('connection_id', db.Integer, db.ForeignKey('zone_connection.id')),
                                     db.Column('port', db.Integer))

    db.mapper(EnvironmentModel, environment_mapping)
    db.mapper(ZoneModel, zone_mapping, properties={
        "environment": db.relationship(EnvironmentModel,
                                       primaryjoin=zone_mapping.c.env_id == environment_mapping.c.id,
                                       backref='zone')
    })
    db.mapper(ZoneConnectionModel, zone_connection_mapping, properties={
        'allowed_ports': db.relationship(AllowedPortModel,
                                         primaryjoin=zone_connection_mapping.c.id == allowed_ports_mapping.c.connection_id,
                                         backref='zone_connection'),
        'source_zone': db.relationship(ZoneModel,
                                       primaryjoin=zone_connection_mapping.c.source_id == zone_mapping.c.id),
        'destination_zone': db.relationship(ZoneModel,
                                            primaryjoin=zone_connection_mapping.c.destination_id == zone_mapping.c.id),
        'firewall': db.relationship(FirewallModel,
                                    primaryjoin=firewall_mapping.c.id == zone_connection_mapping.c.firewall_id)})
    db.mapper(FirewallModel, firewall_mapping)
    db.mapper(AllowedPortModel, allowed_ports_mapping)
