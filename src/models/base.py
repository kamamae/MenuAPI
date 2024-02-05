from sqlalchemy import Column, String
from core.database import Base


class BaseModel(Base):
    __abstract__ = True
    title = Column(String(100), unique=True, nullable=False)
    description = Column(String, nullable=False)
