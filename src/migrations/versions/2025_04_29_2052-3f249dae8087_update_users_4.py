"""Update Users 4

Revision ID: 3f249dae8087
Revises: 6dedd7218b34
Create Date: 2025-04-29 20:52:39.525221

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "3f249dae8087"
down_revision: Union[str, None] = "6dedd7218b34"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "users", "first_name", existing_type=sa.VARCHAR(length=100), nullable=True
    )
    op.alter_column(
        "users", "last_name", existing_type=sa.VARCHAR(length=100), nullable=True
    )


def downgrade() -> None:
    op.alter_column(
        "users", "last_name", existing_type=sa.VARCHAR(length=100), nullable=False
    )
    op.alter_column(
        "users", "first_name", existing_type=sa.VARCHAR(length=100), nullable=False
    )
