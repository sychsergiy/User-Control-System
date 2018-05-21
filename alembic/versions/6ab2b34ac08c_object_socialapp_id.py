"""object_socialapp_id

Revision ID: 6ab2b34ac08c
Revises: aa2120371875
Create Date: 2018-05-21 12:30:01.135174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ab2b34ac08c'
down_revision = 'aa2120371875'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('object', sa.Column('socialapp_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'object', 'socialapp', ['socialapp_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'object', type_='foreignkey')
    op.drop_column('object', 'socialapp_id')
    # ### end Alembic commands ###
