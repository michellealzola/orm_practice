import os
import sys


def create_tables():
    from create_tables import main as create
    create()


def insert_data():
    from insert_suppliers_and_products import main as insert
    insert()


def select_data():
    from select_products import main as select
    select()


def modify_data():
    from modify_and_query_products import main as modify
    modify()


def reset_db():
    from reset_db import main as reset
    reset()


def show_menu():
    print("\n=== ORM Practice Menu ===")
    print("1. Reset database")
    print("2. Create tables")
    print("3. Insert suppliers and products")
    print("4. Query products")
    print("5. Modify/query (Update/Delete/etc.)")
    print("6. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            reset_db()
        elif choice == "2":
            create_tables()
        elif choice == "3":
            insert_data()
        elif choice == "4":
            select_data()
        elif choice == "5":
            modify_data()
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
