"""Add new column phone

Revision ID: f63727146c06
Revises: cc4818e15545
Create Date: 2025-09-18 20:42:49.749214

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f63727146c06'
down_revision: Union[str, Sequence[str], None] = 'cc4818e15545'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(table_name='user', column=sa.Column('phone', sa.String, nullable=False))


def downgrade() -> None:
    op.drop_column(table_name='user', column_name='phone')
