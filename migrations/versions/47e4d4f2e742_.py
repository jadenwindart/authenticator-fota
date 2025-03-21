"""empty message

Revision ID: 47e4d4f2e742
Revises: a476ce4fa2b7
Create Date: 2020-04-12 22:33:57.656231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47e4d4f2e742'
down_revision = 'a476ce4fa2b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('permission', sa.Column('device', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'permission', 'device', ['device'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'permission', type_='foreignkey')
    op.drop_column('permission', 'device')
    # ### end Alembic commands ###
