from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.models import Menu
from core.database import get_async_session
router = APIRouter(
    prefix='/api/v1/menus',
    tags=['menu']
)


@router.get("")
async def get_specific_operations(session: AsyncSession = Depends(get_async_session)):
    query = select(Menu)
    res = await session.execute(query)
    return res.all()
