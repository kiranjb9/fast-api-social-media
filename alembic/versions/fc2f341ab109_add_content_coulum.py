"""Add content coulum

Revision ID: fc2f341ab109
Revises: e5b3b404f24f
Create Date: 2024-02-05 00:30:10.068492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc2f341ab109'
down_revision: Union[str, None] = 'e5b3b404f24f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content', sa.String, nullable=False))


def downgrade() -> None:
    op.drop_column("posts","content")
