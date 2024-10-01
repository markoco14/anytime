"""create user sign in table

Revision ID: 5ce65694c9b2
Revises: a8b973087065
Create Date: 2024-09-30 09:04:57.967077

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ce65694c9b2'
down_revision: Union[str, None] = 'a8b973087065'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('etime_user_signins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('signin_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('ip_address', sa.String(length=45), nullable=True),
    sa.Column('user_agent', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Enum('SUCCESS', 'FAILED', name='signinstatus'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['etime_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_etime_user_signins_id'), 'etime_user_signins', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_etime_user_signins_id'), table_name='etime_user_signins')
    op.drop_table('etime_user_signins')
    # ### end Alembic commands ###