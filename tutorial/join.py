from models import Product
from database import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def show_products_with_supplier():
    products = session.query(Product).all()
    for product in products:
        print(f'{product.name} is supplied by {product.supplier.name}')


if __name__ == '__main__':
    show_products_with_supplier()

