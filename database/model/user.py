from database import Base, db
from sqlalchemy.orm import backref


class User(Base):
    __tablename__ = 'user'

    username = db.Column(db.String(32), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.relationship(
        "Role", backref=backref("role", uselist=False))
