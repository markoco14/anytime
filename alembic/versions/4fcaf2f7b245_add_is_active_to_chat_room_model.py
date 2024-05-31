"""add is_active to chat room model

Revision ID: 4fcaf2f7b245
Revises: 632f916b3235
Create Date: 2024-05-31 18:55:02.677848

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4fcaf2f7b245'
down_revision: Union[str, None] = '632f916b3235'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('etime_chat_rooms', sa.Column('is_active', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('etime_chat_rooms', 'is_active')
    # ### end Alembic commands ###
