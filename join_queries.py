from database import Session
from models import Product, Supplier
from sqlalchemy.orm import joinedload


def main():
    with Session() as session:
        # basic join: get all products with their supplier info
        print('\nJOIN - Products with their suppliers:')
        results = session.query(Product).join(Supplier).all()
        for result in results:
            print(f'{result.name} --> {result.supplier.name}')

        # join with filter: products for Gadget Go only
        print('\nProducts from Gadget Go only:')
        gadget_products = session.query(Product).join(Supplier).filter(Supplier.name == 'Gadget Go').all()
        for gadget_product in gadget_products:
            print(gadget_product.name)

        # Join with add columns: Select specific fields
        print('\nProduct name and Supplier name (via add_columns):')
        named_results = session.query(Product.name, Supplier.name).join(Supplier).all()
        for product_name, supplier_name in named_results:
            print(f'{product_name} --> {supplier_name}')

        # Join with with_entities (alternative to add_columns)
        print('\nProduct + Price using with_entities:')
        entries = session.query(Product).join(Supplier).with_entities(Product.name, Product.price, Supplier.name).all()
        for name, price, supplier_name in entries:
            print(f'{name} --> ${price} --> {supplier_name}')

        # Eager loading using relationship (joinedLoad)
        print('\nEager loaded suppliers:')
        products = session.query(Product).options(joinedload(Product.supplier)).all()
        for product in products:
            print(f'{product.name} --> {product.supplier.name}')


if __name__ == '__main__':
    main()
