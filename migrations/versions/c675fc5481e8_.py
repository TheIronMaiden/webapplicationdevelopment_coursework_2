"""empty message

Revision ID: c675fc5481e8
Revises: 
Create Date: 2018-11-27 12:47:39.849611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c675fc5481e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_nickname'), 'user', ['nickname'], unique=True)
    op.create_index(op.f('ix_user_password'), 'user', ['password'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_password'), table_name='user')
    op.drop_index(op.f('ix_user_nickname'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
