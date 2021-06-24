"""empty message

Revision ID: da5219db52c1
Revises: 
Create Date: 2021-06-22 09:48:02.705413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da5219db52c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('perfil',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('perfil', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('perfil')
    )
    op.create_table('secao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('secao', sa.String(length=10), nullable=False),
    sa.Column('descricao', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('secao')
    )
    op.create_table('produto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.Text(), nullable=False),
    sa.Column('qtde', sa.Integer(), nullable=True),
    sa.Column('preco_unitario', sa.Float(), nullable=False),
    sa.Column('areaid', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['areaid'], ['secao.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome_do_usuario', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('date_created', sa.DateTime(timezone=6), nullable=False),
    sa.Column('last_update', sa.DateTime(timezone=6), nullable=True),
    sa.Column('recovery_code', sa.String(length=100), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('relacao', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['relacao'], ['perfil.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nome_do_usuario')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    op.drop_table('produto')
    op.drop_table('secao')
    op.drop_table('perfil')
    # ### end Alembic commands ###
