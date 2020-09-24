"""empty message

Revision ID: 8ae721ecc756
Revises: 248e29898838
Create Date: 2020-09-23 14:46:22.334209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ae721ecc756'
down_revision = '248e29898838'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'is_admin')
    # ### end Alembic commands ###