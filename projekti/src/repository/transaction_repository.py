

class TransactionsRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def add_income(self,house_id,category_id,amount,description):
        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO transactions (category_id,house_id,amount,description,transaction_type) values (?,?,?,?,"income")',
            (category_id,house_id,amount,description)
        )

        self._connection.commit()
    
    def add_expense(self,house_id,category_id,amount,description):
        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO transactions (category_id,house_id,amount,description,transaction_type) values (?,?,?,?,"expense")',
            (category_id,house_id,amount,description)
        )
        self._connection.commit()
    
    def get_transactions(self):

        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM transactions')

        row = cursor.fetchall()

        return row

    def get_incomes(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM transactions WHERE transaction_type="income"')
        row = cursor.fetchall()
        return row

    def get_expenses(self):
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM transactions WHERE transaction_type="expense"')
        row = cursor.fetchall()
        return row

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('delete from transactions')
        self._connection.commit()