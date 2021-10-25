"""add_email_index

Revision ID: 169a70f86ceb
Revises: 9abd6c35f12c
Create Date: 2021-10-25 01:40:59.227094

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '169a70f86ceb'
down_revision = '9abd6c35f12c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    # ### end Alembic commands ###
