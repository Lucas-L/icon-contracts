"""init

Revision ID: 95c770ca6134
Revises: 
Create Date: 2021-09-21 00:49:06.899676

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '95c770ca6134'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prep',
    sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('country', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('city', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('website', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('details', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('p2p_endpoint', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('node_address', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_prep_address'), 'prep', ['address'], unique=False)
    op.create_index(op.f('ix_prep_city'), 'prep', ['city'], unique=False)
    op.create_index(op.f('ix_prep_country'), 'prep', ['country'], unique=False)
    op.create_index(op.f('ix_prep_details'), 'prep', ['details'], unique=False)
    op.create_index(op.f('ix_prep_email'), 'prep', ['email'], unique=False)
    op.create_index(op.f('ix_prep_id'), 'prep', ['id'], unique=False)
    op.create_index(op.f('ix_prep_name'), 'prep', ['name'], unique=False)
    op.create_index(op.f('ix_prep_node_address'), 'prep', ['node_address'], unique=False)
    op.create_index(op.f('ix_prep_p2p_endpoint'), 'prep', ['p2p_endpoint'], unique=False)
    op.create_index(op.f('ix_prep_website'), 'prep', ['website'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_prep_website'), table_name='prep')
    op.drop_index(op.f('ix_prep_p2p_endpoint'), table_name='prep')
    op.drop_index(op.f('ix_prep_node_address'), table_name='prep')
    op.drop_index(op.f('ix_prep_name'), table_name='prep')
    op.drop_index(op.f('ix_prep_id'), table_name='prep')
    op.drop_index(op.f('ix_prep_email'), table_name='prep')
    op.drop_index(op.f('ix_prep_details'), table_name='prep')
    op.drop_index(op.f('ix_prep_country'), table_name='prep')
    op.drop_index(op.f('ix_prep_city'), table_name='prep')
    op.drop_index(op.f('ix_prep_address'), table_name='prep')
    op.drop_table('prep')
    # ### end Alembic commands ###
