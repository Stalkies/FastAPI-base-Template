"""Fix: Changing user.hashed_password from str to bytes

Revision ID: fefe835965e1
Revises: c1edb993f28d
Create Date: 2025-05-28 22:33:09.165238

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fefe835965e1"
down_revision: Union[str, None] = "c1edb993f28d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "user",
        "hashed_password",
        existing_type=sa.VARCHAR(),
        type_=sa.LargeBinary(),
        existing_nullable=False,
        postgresql_using="hashed_password::bytea",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        "user",
        "hashed_password",
        existing_type=sa.LargeBinary(),
        type_=sa.VARCHAR(),
        existing_nullable=False,
        postgresql_using="encode(hashed_password, 'escape')",
    )
