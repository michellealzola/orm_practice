from database import engine
from models import Base


def main():
    Base.metadata.create_all(engine)
    print('Tables created')


if __name__ == '__main__':
    main()
