from database import Session
from models import Product

session = Session()

print('\nAll Products:')
all_products = session.query(Product).all()
for product in all_products:
    print(product)

print('\nElectronic Products:')
electronics = session.query(Product).filter_by(category='Electronics').all()
for electronic in electronics:
    print(electronic)


