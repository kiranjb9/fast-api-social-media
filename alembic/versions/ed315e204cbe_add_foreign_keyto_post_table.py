"""add foreign keyto post table

Revision ID: ed315e204cbe
Revises: 2403b7d9c66b
Create Date: 2024-02-05 00:41:19.527044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed315e204cbe'
down_revision: Union[str, None] = '2403b7d9c66b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.create_foreign_key('post_user_fk', source_table='posts', referent_table='users',local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('post_user_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
