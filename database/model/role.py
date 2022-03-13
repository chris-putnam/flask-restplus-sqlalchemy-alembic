from database import Base, db


class Role(Base):
    __tablename__ = 'role'

    name = db.Column(db.String(32), nullable=False, unique=True)
