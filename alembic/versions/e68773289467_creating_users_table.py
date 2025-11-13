"""creating users table

Revision ID: e68773289467
Revises: 
Create Date: 2025-11-13 20:06:01.937338

"""
from typing import Sequence, Union
# from sqlalchemy import INTEGER, VARCHAR, NVARCHAR, Column

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e68773289467'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.INTEGER, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("email", sa.String(), nullable=False, unique=True),
    )


def downgrade() -> None:
    op.drop_table("users")
