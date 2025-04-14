from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

# Step 1: set up database connection
engine = create_engine('sqlite:///products.db', echo=True)
Base = declarative_base()


# Step 2: Define ORM class (Table Structure)
class Product(Base):
    __tablename__ = 'products'  # Table name in SQL

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    price = Column(Float)
    quantity = Column(Integer)

    def __repr__(self):
        return f'<Product(id={self.id}, name={self.name}, price={self.price}, quantity={self.quantity})>'


Base.metadata.create_all(engine)
