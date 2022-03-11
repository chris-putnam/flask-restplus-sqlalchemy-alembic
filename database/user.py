from database import Base, db


class User(Base):
    __tablename__ = 'user'

    username = db.Column(db.String(32), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False)
