from repository.house_repository import HouseRepository as default_house_repository
from repository.transaction_repository import TransactionsRepository as default_transaction_repository
from database_connection import get_database_connection

class TransactionService:
    """Transaction service
    """
    def __init__(
     self,
        house_repository=default_house_repository(get_database_connection()),
        transaction_repository=default_transaction_repository(get_database_connection())
        ):
        """init of transaction service

        Args:
            house_repository (class, optional): house repository.
                Defaults to default_house_repository(get_database_connection()).
            transaction_repository (class, optional): transaction repository.
                Defaults to default_transaction_repository(get_database_connection()).
        """
        self.house_repository = house_repository
        self.transaction_repository = transaction_repository

    def add_transaction(self,house_id,category_id,amount,description,transaction_type):
        """Add new transaction to db

        Args:
            house_id (int): house id
            category_id (int): category id
            amount (float): amount
            description (str): description of the new transaction
            transaction_type (str): 'income' or 'expense'
        """
        if transaction_type == 'income':
            self.transaction_repository.add_income(house_id,category_id,amount,description)
        elif transaction_type == 'expense':
            self.transaction_repository.add_expense(house_id,category_id,amount,description)
        else:
            pass

    def get_categories(self):
        """get all transaction categories

        Returns:
            list: list of categories
        """
        return self.transaction_repository.get_categories()

transaction_service = TransactionService()
