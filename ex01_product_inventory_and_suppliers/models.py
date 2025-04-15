from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    contact_email = Column(String(100))

    # One-to-Many relationship: one supplier has many products
    products = relationship('Product', back_populates='supplier')

    def __repr__(self):
        return f'<Supplier(id={self.id}, name={self.name})>'


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    category = Column(String(100))
    price = Column(Float)
    quantity = Column(Integer)

    # Foreign key - points to supplier table
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))

    # Many-to-one relationship: this product belongs to one supplier
    supplier = relationship('Supplier', back_populates='products')

    def __repr__(self):
        return f'<Product(id={self.id}, name={self.name}, supplier={self.supplier.name if self.supplier else None})>'
