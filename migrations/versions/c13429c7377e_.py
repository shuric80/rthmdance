"""empty message

Revision ID: c13429c7377e
Revises: None
Create Date: 2016-10-13 22:27:01.060066

"""

# revision identifiers, used by Alembic.
revision = 'c13429c7377e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('content',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Unicode(length=512), nullable=True),
    sa.Column('text', sa.Text(length=10000), nullable=True),
    sa.Column('tstamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('email',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.Unicode(length=1024), nullable=True),
    sa.Column('text', sa.Text(length=5000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('superuser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.Unicode(length=128), nullable=True),
    sa.Column('email', sa.Unicode(length=128), nullable=True),
    sa.Column('_password_hash', sa.Unicode(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=128), nullable=False),
    sa.Column('tel', sa.Unicode(length=20), nullable=False),
    sa.Column('email', sa.Unicode(length=64), nullable=False),
    sa.Column('message', sa.Unicode(length=1024), nullable=True),
    sa.Column('tstamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('superuser')
    op.drop_table('email')
    op.drop_table('content')
    ### end Alembic commands ###
