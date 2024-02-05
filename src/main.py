from fastapi import FastAPI
from api.router import router as router_operation
app = FastAPI(
    title="Menu"
)

app.include_router(router_operation)



#
#
# """add_index
#
# Revision ID: cc93925cda8f
# Revises: 5015f6bc7801
# Create Date: 2024-02-01 22:52:12.495295
#
# """
# from typing import Sequence, Union
#
# from alembic import op
# import sqlalchemy as sa
#
#
# # revision identifiers, used by Alembic.
# revision: str = 'cc93925cda8f'
# # down_revision: Union[str, None] = '5015f6bc7801'
# branch_labels: Union[str, Sequence[str], None] = None
# depends_on: Union[str, Sequence[str], None] = None
#
#
#
# def upgrade() -> None:
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.create_index(op.f('ix_dishes_id'), 'dishes', ['id'], unique=False)
#     op.create_index(op.f('ix_menus_id'), 'menus', ['id'], unique=False)
#     op.create_index(op.f('ix_submenus_id'), 'submenus', ['id'], unique=False)
#     # ### end Alembic commands ###
#
#
# def downgrade() -> None:
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.drop_index(op.f('ix_submenus_id'), table_name='submenus')
#     op.drop_index(op.f('ix_menus_id'), table_name='menus')
#     op.drop_index(op.f('ix_dishes_id'), table_name='dishes')
#     # ### end Alembic commands ###
