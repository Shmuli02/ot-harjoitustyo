from repository.transaction_repository import TransactionsRepository

class House:
    def __init__(self,id,houseName,address,expenses=[],incomes=[]):
        self.id = id
        self.name = houseName
        self.address = address
        self.expenses = expenses
        self.incomes = incomes

    def add_expense(self,amount,category,description):
        if amount>0:
            self.expenses.append({'amount':amount,'category':category,'description':description})

    def add_income(self,amount,category,description):
        if amount>0:
            self.incomes.append({'amount':amount,'category':category,'description':description})

    def edit_expense(self):
        pass

    def edit_income(self):
        pass

    def house_report(self):
        incomes = sum([i.amount for i in self.incomes])
        expenses = sum([i.amount for i in self.expenses])
        profit = incomes-expenses
        
        return {'incomes':incomes,'expenses':expenses,'profit':profit}