from models import Product
from database import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def show_low_stock():
    low_stock = session.query(Product).filter(Product.quantity < 30).all()
    for product in low_stock:
        print(f'{product.name}: {product.quantity} in stock')


if __name__ == '__main__':
    show_low_stock()
