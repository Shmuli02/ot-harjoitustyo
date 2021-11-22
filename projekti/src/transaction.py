class Transaction:
    def __init__(self,house_id,category_id,amount,description,transaction_type):
        self.house_id = house_id
        self.category = category_id
        self.amount = amount
        self.description = description
        self.transaction_type = transaction_type
