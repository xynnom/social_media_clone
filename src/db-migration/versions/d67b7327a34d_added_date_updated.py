"""Added date_updated

Revision ID: d67b7327a34d
Revises: de38d67beff3
Create Date: 2022-02-18 22:42:19.264963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd67b7327a34d'
down_revision = 'de38d67beff3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('date_updated', sa.DateTime(), nullable=True))
    op.add_column('posts', sa.Column('date_updated', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'date_updated')
    op.drop_column('comments', 'date_updated')
    # ### end Alembic commands ###
