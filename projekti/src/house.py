from repository.transaction_repository import TransactionsRepository
from database_connection import get_database_connection

class House:
    def __init__(self,id,houseName,address,expenses=[],incomes=[]):
        self.id = id
        self.name = houseName
        self.address = address
        self.expenses = expenses
        self.incomes = incomes
        self._transaction_repository = TransactionsRepository(get_database_connection())

    


    def add_income(self,category_id,amount,description):
        if int(amount)>0:
            new_transaction = self._transaction_repository.add_income(self.id,category_id,amount,description)
            return True
        else:
            return False
    
    def add_expense(self,category_id,amount,description):
        if int(amount)>0:
            new_transaction = self._transaction_repository.add_expense(self.id,category_id,amount,description)
            return True
        else:
            return False

    def edit_expense(self):
        pass

    def edit_income(self):
        pass

    def house_report(self):
        incomes = sum([i.amount for i in self.incomes])
        expenses = sum([i.amount for i in self.expenses])
        report_values = {'incomes':incomes,'expenses':expenses}
        return report_values