import uuid
from sqlalchemy import Column, Float, ForeignKey, MetaData, String, UniqueConstraint, func, select, and_
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, column_property
from .base import BaseModel


metadata = MetaData()


class Dish(BaseModel):
    __tablename__ = "dishes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    submenu_id = Column(
        ForeignKey("submenus.id", ondelete="CASCADE"),
        nullable=False,
    )
    price = Column(Float)


class SubMenu(BaseModel):
    __tablename__ = "submenus"

    id = Column(String, primary_key=True, default=uuid.uuid4, index=True)
    menu_id = Column(UUID(as_uuid=True), ForeignKey("menus.id"))
    dishes = relationship("Dish", cascade="delete", backref="submenu", lazy="selectin")
    dishes_count = column_property(
        select(func.count(Dish.id)).where(Dish.submenu_id == id).scalar_subquery(),
    )


class Menu(BaseModel):
    __tablename__ = "menus"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)

    submenus = relationship(
        "SubMenu", cascade="delete", backref="menu", lazy="selectin"
    )
    submenus_count = column_property(
        select(func.count(SubMenu.id)).where(SubMenu.menu_id == id).scalar_subquery(),
    )

    dishes_count = column_property(
        select(func.count(Dish.id))
        .join(SubMenu)
        .where(and_(SubMenu.menu_id == id, SubMenu.id == Dish.submenu_id))
        .correlate_except(Dish)
        .scalar_subquery()
    )
