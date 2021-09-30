"""init

Revision ID: 6e054c85f163
Revises:
Create Date: 2021-09-29 19:48:01.889089

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "6e054c85f163"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "contract",
        sa.Column("abi", sa.JSON(), nullable=True),
        sa.Column("address", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("symbol", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("decimals", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("contract_type", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("country", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("city", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("email", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("website", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("details", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("p2p_endpoint", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("node_address", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("last_updated_block", sa.Integer(), nullable=True),
        sa.Column("last_updated_timestamp", sa.Integer(), nullable=True),
        sa.Column("created_block", sa.Integer(), nullable=True),
        sa.Column("created_timestamp", sa.Integer(), nullable=True),
        sa.Column("current_version", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("status", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.PrimaryKeyConstraint("address"),
    )
    op.create_index(op.f("ix_contract_address"), "contract", ["address"], unique=False)
    op.create_index(op.f("ix_contract_contract_type"), "contract", ["contract_type"], unique=False)
    op.create_index(op.f("ix_contract_created_block"), "contract", ["created_block"], unique=False)
    op.create_index(
        op.f("ix_contract_created_timestamp"), "contract", ["created_timestamp"], unique=False
    )
    op.create_index(
        op.f("ix_contract_last_updated_block"), "contract", ["last_updated_block"], unique=False
    )
    op.create_index(
        op.f("ix_contract_last_updated_timestamp"),
        "contract",
        ["last_updated_timestamp"],
        unique=False,
    )
    op.create_index(op.f("ix_contract_status"), "contract", ["status"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_contract_status"), table_name="contract")
    op.drop_index(op.f("ix_contract_last_updated_timestamp"), table_name="contract")
    op.drop_index(op.f("ix_contract_last_updated_block"), table_name="contract")
    op.drop_index(op.f("ix_contract_created_timestamp"), table_name="contract")
    op.drop_index(op.f("ix_contract_created_block"), table_name="contract")
    op.drop_index(op.f("ix_contract_contract_type"), table_name="contract")
    op.drop_index(op.f("ix_contract_address"), table_name="contract")
    op.drop_table("contract")
    # ### end Alembic commands ###