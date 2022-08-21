from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

# from app.db.base_class import Base

from mongoengine import Document, IntField, StringField, ListField, BooleanField

# if TYPE_CHECKING:
#     from .item import Item  # noqa: F401


class Users(Document):
    full_name = StringField(max_length=125)
    email = StringField(max_length=125)
    hashed_password = StringField(max_length=125)
    is_active = BooleanField(default=False)
    # is_superuser = Column(Boolean(), default=False)
    # items = relationship("Item", back_populates="owner")

