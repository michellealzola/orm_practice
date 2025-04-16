from models import Supplier, Product
from database import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def insert_data():
    supplier1 = Supplier(name="Tech Source", contact_email="tech@source.com")
    supplier2 = Supplier(name="Office Hub", contact_email="contact@officehub.com")

    product1 = Product(name="Keyboard", category="Electronics", price=29.99, quantity=50, supplier=supplier1)
    product2 = Product(name="Office Chair", category="Furniture", price=89.50, quantity=20, supplier=supplier2)
    product3 = Product(name="Monitor 24\"", category="Electronics", price=199.00, quantity=10, supplier=supplier1)

    session.add_all([supplier1, supplier2, product1, product2, product3])
    session.commit()
    print('Records are inserted successfully')


if __name__ == '__main__':
    insert_data()
