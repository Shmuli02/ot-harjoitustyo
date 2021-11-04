from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists house;
    ''')
    cursor.execute('''
        drop table if exists incomeExpense;
    ''')
    cursor.execute('''
        drop table if exists category;
    ''')

            
        

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table house (
            house_id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT
        );

    ''')
    cursor.execute('''
        create table incomeExpense (
            incomeExpense_id INTEGER PRIMARY KEY,
            category_id INTEGER,
            house_id INTEGER,
            amount INTEGER,
            income BOOLEAN,
            expense BOOLEAN
        );

    ''')
    cursor.execute('''
        create table category (
            category_id INTEGER PRIMARY KEY,
            category TEXT
        );

    ''')


    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
