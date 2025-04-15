from database import Session
from models import Supplier, Product

session = Session()

# Create suppliers
s1 = Supplier(name='Gadget Go', contact_email='sales@gadgetgo.com')
s2 = Supplier(name='HomeGoods Inc.', contact_email='hello@homegoods.com')

# Create products and assign supplier via relationship
p1 = Product(name='Wireless Mouse', category='Electronics', price=25.99, quantity=100, supplier=s1)
p2 = Product(name="USB-C Cable", category="Electronics", price=9.99, quantity=300, supplier=s1)
p3 = Product(name="Coffee Mug", category="Kitchenware", price=12.50, quantity=150, supplier=s2)

# add and commit
session.add_all([s1, s2, p1, p2, p3])
session.commit()

print('Suppliers and Products inserted')

# query products with their supplier
products = session.query(Product).all()
for product in products:
    print(f'{product.name} supplied by {product.supplier.name}')

