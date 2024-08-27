"""add timestamp fields to DbShare model

Revision ID: a8b973087065
Revises: 5f30b87e029c
Create Date: 2024-08-25 15:46:51.377316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text
from datetime import datetime, timedelta


# revision identifiers, used by Alembic.
revision: str = 'a8b973087065'
down_revision: Union[str, None] = '5f30b87e029c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('etime_shares', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('etime_shares', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))

    # Get the current timestamp
    now = datetime.now()

    connection = op.get_bind()

    # Get the maximum id from the etime_shares table
    # Get all the ids from the etime_shares table
    result = connection.execute(
        text("SELECT id FROM etime_shares ORDER BY id ASC"))
    ids = [row[0] for row in result]

    if not ids:
        return  # No rows to update


    # Calculate the time difference between each row
    time_diff = timedelta(seconds=1)

    # Iterate over each row and set the created_at timestamp
    for index, id in enumerate(ids):
        created_at = now - (len(ids) - index) * time_diff
        connection.execute(
            text("UPDATE etime_shares SET created_at = :created_at WHERE id = :id"),
            {"created_at": created_at, "id": id}
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('etime_shares', 'updated_at')
    op.drop_column('etime_shares', 'created_at')
    # ### end Alembic commands ###