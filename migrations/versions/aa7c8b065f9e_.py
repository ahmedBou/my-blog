"""empty message

Revision ID: aa7c8b065f9e
Revises: 8af052f21f3c
Create Date: 2018-11-11 19:12:53.415429

"""

# revision identifiers, used by Alembic.
revision = 'aa7c8b065f9e'
down_revision = '8af052f21f3c'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('author', 'is_author',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.add_column('post', sa.Column('category_id', sa.Integer(), nullable=True))
    op.alter_column('post', 'live',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.Boolean(),
               existing_nullable=True)
    op.create_foreign_key(None, 'post', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.alter_column('post', 'live',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    op.drop_column('post', 'category_id')
    op.alter_column('author', 'is_author',
               existing_type=sa.Boolean(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=True)
    # ### end Alembic commands ###
