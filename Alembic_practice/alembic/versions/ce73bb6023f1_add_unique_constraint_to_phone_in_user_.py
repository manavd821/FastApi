"""Add unique constraint to phone in user table

Revision ID: ce73bb6023f1
Revises: f63727146c06
Create Date: 2025-09-18 20:59:56.785445

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ce73bb6023f1'
down_revision: Union[str, Sequence[str], None] = 'f63727146c06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('user') as batch_op:
        batch_op.create_unique_constraint('uq_user_phone', ['phone'])


def downgrade() -> None:
    with op.batch_alter_table('user') as batch_op:
        batch_op.drop_constraint(constraint_name='uq_user_phone',type_='unique')