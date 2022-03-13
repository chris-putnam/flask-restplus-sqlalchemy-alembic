from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

metadata = db.metadata
declarative_base = db.make_declarative_base(db.Model, metadata=db.metadata)


class Base(declarative_base):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
