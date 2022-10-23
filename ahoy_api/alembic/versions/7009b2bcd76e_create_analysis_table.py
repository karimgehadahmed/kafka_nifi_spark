"""create analysis table

Revision ID: 7009b2bcd76e
Revises: 
Create Date: 2022-10-21 21:31:59.487243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7009b2bcd76e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "analysis_data",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("date_time", sa.DateTime(), nullable=True),
        sa.Column("average_rating", sa.Float(), nullable=True),
        sa.Column("total_count", sa.Integer(), nullable=True),
        sa.Column("max_rating", sa.Float(), nullable=True),
        sa.Column("min_rating", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_analysis_data_id"),
        "analysis_data",
        ["id"],
        unique=False,
    )


def downgrade():
    op.drop_index(op.f("ix_analysis_data_id"), table_name="analysis_data")
    op.drop_table("analysis_data")
