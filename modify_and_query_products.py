from database import Session
from models import Product
from sqlalchemy import func


def main():
    session = Session()

    product_name = 'Coffee Mug'

    # Update product
    print(f'\nUpdating Product: {product_name}')
    product = session.query(Product).filter_by(name=product_name).first()
    if product:
        product.price = 11.00
        product.quantity = 200
        session.commit()
        print(f'\nProduct {product_name} updated')
    else:
        print(f'\nProduct {product_name} not found')

    # Delete product
    product_name = 'Notebook'
    print(f'\nDeleting Product: {product_name}')
    product_to_delete = session.query(Product).filter_by(name=product_name).first()
    if product_to_delete:
        session.delete(product_to_delete)
        session.commit()
        print(f'\nProduct {product_name} deleted')
    else:
        print(f'\nProduct {product_name} not found')

    # Count all products
    print('\nTotal Products in Table:')
    product_count = session.query(func.count(Product.id)).scalar()
    print(f'\nTotal Products in Table: {product_count}')

    # Order products by price descending
    print('\nProducts Ordered by Price (High to Low):')
    ordered = session.query(Product).order_by(Product.price.desc()).all()
    for p in ordered:
        print(f'{p}')

    # Limit to 2 products only
    print('\nFirst 2 products only:')
    limited = session.query(Product).limit(2).all()
    for p in limited:
        print(f'{p}')

if __name__ == '__main__':
    main()