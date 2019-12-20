"""empty message

Revision ID: a71b7c9424bc
Revises: 
Create Date: 2019-12-15 15:55:59.239148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a71b7c9424bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('migrate_version')
    op.add_column('user', sa.Column('password', sa.String(length=30), nullable=True))
    op.create_index(op.f('ix_user_password'), 'user', ['password'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_password'), table_name='user')
    op.drop_column('user', 'password')
    op.create_table('migrate_version',
    sa.Column('repository_id', sa.VARCHAR(length=250), nullable=False),
    sa.Column('repository_path', sa.TEXT(), nullable=True),
    sa.Column('version', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('repository_id')
    )
    # ### end Alembic commands ###