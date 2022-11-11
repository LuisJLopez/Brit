from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100))
    price = Column(Float(precision=2))

    def __repr__(self):
        return f"{self.name}-£{self.price}"
