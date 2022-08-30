from sqlalchemy import Column, Float, Integer, String

from app.core import database


class Product(database.Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
