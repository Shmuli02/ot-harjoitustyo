class House:
    def __init__(self,houseName,address,expenses=[],incomes=[]):
        self.name = houseName
        self.address = address
        self.expenses = expenses
        self.incomes = incomes

    def addExpense(self,amount,category,description):
        if amount>0:
            self.expenses.append({'amount':amount,'category':category,'description':description})

    def addIncome(self,amount,category,description):
        if amount>0:
            self.incomes.append({'amount':amount,'category':category,'description':description})

    def editExpense(self):
        pass

    def editIncome(self):
        pass

    def houseReport(self):
        incomes = sum([i.amount for i in self.incomes])
        expenses = sum([i.amount for i in self.expenses])
        profit = incomes-expenses
        
        return {'incomes':incomes,'expenses':expenses,'profit':profit}