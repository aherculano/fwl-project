from flask_sqlalchemy import SQLAlchemy


# TODO : GENERALIZE

class SQLAlchemyBase(object):

    def __init__(self, db: SQLAlchemy):
        self.db = db
