"""add likes column to Product

Revision ID: 043f4e390952
Revises: 514b5e9fbcff
Create Date: 2025-05-25 08:13:10.731298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '043f4e390952'
down_revision = '514b5e9fbcff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('likes', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_column('likes')

    # ### end Alembic commands ###
