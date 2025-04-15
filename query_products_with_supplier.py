from database import Session
from models import Product, Supplier

session = Session()

print('\nProducts and their Suppliers:')
# query products with their supplier
products = session.query(Product).all()
for product in products:
    print(f'{product.name} supplied by {product.supplier.name}')


