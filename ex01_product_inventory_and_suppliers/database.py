from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///my_store.db')

Session = sessionmaker(bind=engine)
