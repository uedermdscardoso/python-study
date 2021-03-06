"""empty message

Revision ID: 92858d026b4a
Revises: 4fd0ed273bab
Create Date: 2020-09-23 04:15:43.205955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92858d026b4a'
down_revision = '4fd0ed273bab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('funcionario_projeto',
    sa.Column('projeto_id', sa.Integer(), nullable=False),
    sa.Column('funcionario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['funcionario_id'], ['funcionario.id'], ),
    sa.ForeignKeyConstraint(['projeto_id'], ['projeto.id'], ),
    sa.PrimaryKeyConstraint('projeto_id', 'funcionario_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('funcionario_projeto')
    # ### end Alembic commands ###
