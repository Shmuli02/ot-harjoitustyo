from repository.transaction_repository import TransactionsRepository
from database_connection import get_database_connection

class House:
    def __init__(self,id,houseName,address,expenses=None,incomes=None):
        self.id = id
        self.name = houseName
        self.address = address
        self.expenses = [] if expenses is None else expenses
        self.incomes = [] if incomes is None else incomes
        self._transaction_repository = TransactionsRepository(get_database_connection())

    def add_income(self,category_id,amount,description):
        new_transaction = self._transaction_repository.add_income(self.id,category_id,amount,description)
        return True

    def add_expense(self,category_id,amount,description):
        new_transaction = self._transaction_repository.add_expense(self.id,category_id,amount,description)
        return True

    def house_report(self):
        incomes = sum([i.amount for i in self.incomes])
        expenses = sum([i.amount for i in self.expenses])
        report_values = {'incomes':incomes,'expenses':expenses}
        return report_values
