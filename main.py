from sql.create_tables import create_tables
from sql.sample_data import insert_sample_data
from menu import main_menu


def main():

    create_tables()

    insert_sample_data()

    main_menu()


if __name__=="__main__":
    main()