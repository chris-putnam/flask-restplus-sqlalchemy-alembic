"""Seed users

Revision ID: 440aa72c7f23
Revises: d6649fc2f7eb
Create Date: 2022-03-12 21:32:26.608901

"""
from alembic import op
import sqlalchemy as sa

from database import Base, user


# revision identifiers, used by Alembic.
revision = '440aa72c7f23'
down_revision = 'd6649fc2f7eb'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)
    user1 = user.User(username='chris', email='chris.putnam@swedenstreet.com')
    session.add(user1)
    session.commit()
    pass


def downgrade():
    pass
