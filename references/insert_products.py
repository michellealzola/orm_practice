from database import Session
from models import Product

session = Session()

product1 = Product(name='Wireless Mouse', category='Electronics', price=25.99, quantity=100)
product2 = Product(name='Coffee Mug', category='Kitchenware', price=9.50, quantity=250)
product3 = Product(name='Notebook', category='Stationery', price=2.25, quantity=500)

session.add_all([product1, product2, product3])
session.commit()

print('Sample products inserted')

