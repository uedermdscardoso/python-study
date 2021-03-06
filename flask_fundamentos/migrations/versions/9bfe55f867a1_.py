"""empty message

Revision ID: 9bfe55f867a1
Revises: 
Create Date: 2020-09-22 20:04:28.873027

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from app.models.cliente_model import Cliente

revision = '9bfe55f867a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clientes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('data_nascimento', sa.DateTime(), nullable=True),
    sa.Column('profissao', sa.String(length=30), nullable=True),
    sa.Column('genero', sqlalchemy_utils.types.choice.ChoiceType(Cliente.GENERO_CHOICES), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clientes')
    # ### end Alembic commands ###
