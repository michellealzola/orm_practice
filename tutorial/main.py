import create_tables
import insert_records
import join
import filter
import update
import delete


def run_all():
    print(f'Creating tables...')
    create_tables.create_tables()
    print(f'Inserting records...')
    insert_records.insert_data()
    print(f'Joining tables...')
    join.show_products_with_supplier()
    print(f'Showing low stock products...')
    filter.show_low_stock()
    print(f'Updating product price...')
    update.update_price()
    print(f'Delete product records...')
    delete.delete_product()


if __name__ == '__main__':
    run_all()
