from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    category = Column(String(50))
    price = Column(Float)
    quantity = Column(Integer)

    def __repr__(self):
        return (f'<Product(id={self.id}, name={self.name}, category={self.category}, '
                f'price={self.price}, quantity={self.quantity})>')
