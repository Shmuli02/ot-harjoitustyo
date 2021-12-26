from transaction import Transaction

def get_transactions_by_row(row):
    return Transaction(
        row['house_id'],
        row['category_id'],
        row['amount'],
        row['description'],
        row['transaction_type']) if row else None

def get_categories_by_row(row):
    return {'category_id':row['category_id'],'category':row['category']}


class TransactionsRepository:
    """Transaction repository that handle transaction db
    """
    def __init__(self, connection):
        """init transaction repository

        Args:
            connection: db connection
        """
        self._connection = connection

    def add_income(self,house_id,category_id,amount,description):
        """Add new income to db

        Args:
            house_id (int): id of the house
            category_id (int): category of the income
            amount (float): amount
            description (str): description of the income

        Returns:
            int: id of the new income
        """
        cursor = self._connection.cursor()
        amount = float(str(amount).replace(',','.'))
        if house_id != '' and category_id != '':
            cursor.execute(
                '''
                INSERT INTO transactions
                (category_id,house_id,amount,description,transaction_type)
                values
                (?,?,?,?,"income")
                ''',
                (category_id,house_id,amount,description)
            )

            self._connection.commit()
            return cursor.lastrowid

    def add_expense(self,house_id,category_id,amount,description):
        """Add new expense to db

        Args:
            house_id (int): id of the house
            category_id (int): category of the expense
            amount (float): amount
            description (str): description of expense

        Returns:
            int: return id of the new expense
        """
        cursor = self._connection.cursor()
        amount = float(str(amount).replace(',','.'))
        if house_id != '' and category_id != '':
            cursor.execute(
                '''
                INSERT INTO transactions
                (category_id,house_id,amount,description,transaction_type)
                values (?,?,?,?,"expense")
                ''',
                (category_id,house_id,amount,description)
            )
            self._connection.commit()
            return cursor.lastrowid
        return

    def get_transactions(self):
        """get all transaction

        Returns:
            list: all transactions
        """

        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM transactions')

        row = cursor.fetchall()

        return list(map(get_transactions_by_row,row))

    def get_incomes(self):
        """get all incomes

        Returns:
            list: list of expenses
        """
        cursor = self._connection.cursor()
        cursor.execute(
            '''
            SELECT * FROM transactions
            WHERE transaction_type="income"
            ''')
        row = cursor.fetchall()
        return list(map(get_transactions_by_row,row))

    def get_expenses(self):
        """get all expenses

        Returns:
            list: list of expenses
        """
        cursor = self._connection.cursor()
        cursor.execute(
            '''
            SELECT * FROM transactions
            WHERE transaction_type="expense"
            ''')
        row = cursor.fetchall()
        return list(map(get_transactions_by_row,row))

    def edit_income(self,transaction_id,house_id,category_id,amount,description):
        """Edit income

        Args:
            transaction_id (int): transaction id to edit
            house_id (int): house id
            category_id (int): category id
            amount (float): amount
            description (str): description of the income
        """
        cursor = self._connection.cursor()
        amount = float(str(amount).replace(',','.'))
        cursor.execute(
            '''
            UPDATE transactions
            SET transaction_id=?, category_id=?, house_id=?, amount=?, description=?
            ''',
            (transaction_id,category_id,house_id,amount,description)
        )
        self._connection.commit()

    def edit_expense(self,transaction_id,house_id,category_id,amount,description):
        """Edit expense

        Args:
            transaction_id (int): transaction id to edit
            house_id (int): house id
            category_id (int): category id
            amount (float): amount
            description (str): description of the expense
        """
        cursor = self._connection.cursor()
        amount = float(str(amount).replace(',','.'))
        cursor.execute(
            '''
            UPDATE transactions
            SET transaction_id=?, category_id=?, house_id=?, amount=?, description=?
            ''',
            (transaction_id,category_id,house_id,amount,description)
        )
        self._connection.commit()

    def delete_all(self):
        """Delete all transactions from db
        """
        cursor = self._connection.cursor()
        cursor.execute('delete from transactions')
        self._connection.commit()

    def get_categories(self):
        """get all categories

        Returns:
            list: all categories
        """
        cursor = self._connection.cursor()
        cursor.execute('SELECT * from category')
        rows = cursor.fetchall()
        return list(map(get_categories_by_row,rows))
