"""empty message

Revision ID: ddcf5eebf1dc
Revises: a09d118c216b
Create Date: 2019-12-15 16:11:57.121400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddcf5eebf1dc'
down_revision = 'a09d118c216b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_password', table_name='user')
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=30), nullable=True))
    op.create_index('ix_user_password', 'user', ['password'], unique=False)
    # ### end Alembic commands ###
