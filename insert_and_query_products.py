from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///store.db', echo=True)
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


# Step 3: Create table if it does not exist
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# 4: Insert Sample Products
product1 = Product(name='Wireless Mouse', category='Electronics', price=25.99, quantity=100)
product2 = Product(name='Coffee Mug', category='Kitchenware', price=9.5, quantity=250)
product3 = Product(name='Notebook', category='Stationery', price=2.25, quantity=500)

# Step 5: Add and commit to database
session.add_all([product1, product2, product3])
session.commit()

# Step 6: Query and print all products
print('\nAll Products in Database:')
all_products = session.query(Product).all()
for product in all_products:
    print(product)
