from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists house;
    ''')
    cursor.execute('''
        drop table if exists transactions;
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
        create table transactions (
            transaction_id INTEGER PRIMARY KEY,
            category_id INTEGER,
            house_id INTEGER,
            amount INTEGER,
            description TEXT,
            transaction_type TEXT
            
        );

    ''')
    cursor.execute('''
        create table category (
            category_id INTEGER PRIMARY KEY,
            category TEXT
        );

    ''')

    connection.commit()

def add_categories(connection):
    cursor = connection.cursor()
    categories_to_add = [(1,'Yhtiövastike'),(2,'Pääomavastike'),(3,'Vesi'),(4,'Sähkö'),(5,'Vuokra tulo')]
    cursor.executemany('INSERT INTO category VALUES (?,?)',categories_to_add)
    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    add_categories(connection)



if __name__ == "__main__":
    initialize_database()
