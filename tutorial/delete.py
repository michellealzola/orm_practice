from models import Product
from database import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def delete_product():
    product = session.query(Product).filter_by(name='Keyboard').first()
    if product:
        session.delete(product)
        session.commit()
        print(f'{product.name} deleted from inventory')
    else:
        print(f'{product.name} not found')


if __name__ == '__main__':
    delete_product()
