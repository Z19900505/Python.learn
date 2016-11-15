"""timestamp

Revision ID: 1381d0bd5ca
Revises: cbf66625da
Create Date: 2015-12-28 16:14:25.396412

"""

# revision identifiers, used by Alembic.
revision = '1381d0bd5ca'
down_revision = 'cbf66625da'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activity', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_activity_actor_id'), 'activity', ['actor_id'], unique=False)
    op.create_index(op.f('ix_activity_timestamp'), 'activity', ['timestamp'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_activity_timestamp'), table_name='activity')
    op.drop_index(op.f('ix_activity_actor_id'), table_name='activity')
    op.drop_column('activity', 'timestamp')
    ### end Alembic commands ###