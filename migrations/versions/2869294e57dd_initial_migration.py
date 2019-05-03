"""Initial Migration

Revision ID: 2869294e57dd
Revises: 
Create Date: 2019-05-02 16:32:12.465548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2869294e57dd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
