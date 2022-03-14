"""Seed roles

Revision ID: c2314f0719fb
Revises: 0f183d463b40
Create Date: 2022-03-13 16:23:29.086117

"""
from alembic import op
import sqlalchemy as sa

from database.model import Role


# revision identifiers, used by Alembic.
revision = 'c2314f0719fb'
down_revision = '0f183d463b40'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)

    admin_role = Role(name='Administrator')
    session.add(admin_role)

    manager_role = Role(name='Manager')
    session.add(manager_role)

    session.commit()
    pass


def downgrade():
    pass
