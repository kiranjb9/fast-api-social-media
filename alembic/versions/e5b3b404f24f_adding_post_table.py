"""adding post table

Revision ID: e5b3b404f24f
Revises: 
Create Date: 2024-02-05 00:13:26.479296

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e5b3b404f24f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_column('posts')
