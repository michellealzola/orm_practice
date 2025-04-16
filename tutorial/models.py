from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey

Base = declarative_base()


class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    contact_email = Column(String)

    # relationship
    products = relationship('Product', back_populates='supplier')


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

    # Foreign key
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

    # relationship
    supplier = relationship('Supplier', back_populates='products')
