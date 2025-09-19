"""create a user table

Revision ID: cc4818e15545
Revises: 
Create Date: 2025-09-18 19:31:47.636033

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String


# revision identifiers, used by Alembic.
revision: str = 'cc4818e15545'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "user",
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("email", String(200)),
)


def downgrade() -> None:
    op.drop_table(table_name='user', if_exists=True)
