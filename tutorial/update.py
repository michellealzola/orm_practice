from models import Product
from database import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def update_price():
    product = session.query(Product).filter_by(name='Office Chair').first()
    if product:
        product.price = 95.00
        session.commit()
        print(f'Updated {product.name} to ${product.price}')
    else:
        print(f'No product {product.name}')


if __name__ == '__main__':
    update_price()
