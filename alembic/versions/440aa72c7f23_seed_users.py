"""Seed users

Revision ID: 440aa72c7f23
Revises: d6649fc2f7eb
Create Date: 2022-03-12 21:32:26.608901

"""
from alembic import op
import sqlalchemy as sa

from database.model import User, Role


# revision identifiers, used by Alembic.
revision = '440aa72c7f23'
down_revision = '4945c38fa385'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)

    admin_role = session.query(Role).filter(
        Role.name == 'Administrator').first()
    manager_role = session.query(Role).filter(Role.name == 'Manager').first()

    user1 = User(username='chris',
                 email='chris.putnam@email.com', role=admin_role)
    session.add(user1)

    user1 = User(username='man',
                 email='man.ager@email.com', role=manager_role)
    session.add(user1)

    session.commit()
    pass


def downgrade():
    pass
