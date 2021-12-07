from repository.house_repository import HouseRepository as default_house_repository
from repository.transaction_repository import TransactionsRepository as default_transaction_repository
from database_connection import get_database_connection

class TransactionService:
    def __init__(
     self,
        house_repository=default_house_repository(get_database_connection()),
        transaction_repository=default_transaction_repository(get_database_connection())
        ):
        self.house_repository = house_repository
        self.transaction_repository = transaction_repository

    def add_transaction(self,house_id,category_id,amount,description,transaction_type):
        if transaction_type == 'income':
            self.transaction_repository.add_income(house_id,category_id,amount,description)
        elif transaction_type == 'expense':
            self.transaction_repository.add_expense(house_id,category_id,amount,description)
        else:
            pass

    def get_categories(self):
        return self.transaction_repository.get_categories()

transaction_service = TransactionService()
