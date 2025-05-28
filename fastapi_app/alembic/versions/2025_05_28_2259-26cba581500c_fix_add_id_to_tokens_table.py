"""Fix: Add id to tokens table

Revision ID: 26cba581500c
Revises: fefe835965e1
Create Date: 2025-05-28 22:59:37.754314

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "26cba581500c"
down_revision: Union[str, None] = "fefe835965e1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("token", sa.Column("id", sa.Integer(), nullable=False))
    op.create_index(op.f("ix_token_id"), "token", ["id"], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_token_id"), table_name="token")
    op.drop_column("token", "id")
