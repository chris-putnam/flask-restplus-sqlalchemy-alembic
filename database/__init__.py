from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Base = db
metadata = Base.metadata


class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
