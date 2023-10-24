"""empty message

Revision ID: 3680b59de891
Revises: fe5653d929cb
Create Date: 2023-10-22 19:26:05.447824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3680b59de891'
down_revision = 'fe5653d929cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nombre', sa.String(length=80), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('nombre')

    # ### end Alembic commands ###
