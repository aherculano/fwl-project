from flask_sqlalchemy import SQLAlchemy

# TODO : GENERALIZE
from sqlalchemy.exc import IntegrityError, OperationalError, DatabaseError


class SQLAlchemyBase(object):

    def __init__(self, db: SQLAlchemy):
        self.db = db

    def add(self, schema):
        try:
            self.db.session.add(schema)
            self.db.session.commit()
            return schema
        except IntegrityError as ie:
            self.db.session.rollback()
            raise ie
        except OperationalError as oe:
            self.db.session.rollback()
            raise oe

    def get_by_filter(self, cls, cls_filter, attribute):
        try:
            schema = self.db.session.query(cls).filter(cls_filter == attribute).first()
        except DatabaseError as de:
            raise de
        if schema:
            return schema
        else:
            raise ValueError("NOT FOUND")

    def list(self, cls):
        try:
            cls_list: [cls] = self.db.session.query(cls).all()
            return cls_list
        except DatabaseError as de:
            raise de

    def delete(self, schema):
        self.db.session.query(schema).delete()
        self.db.session.commit()

    def exists(self, cls, cls_filter, attribute):
        return self.db.session.query(cls).filter(cls_filter == attribute).first() is not None
