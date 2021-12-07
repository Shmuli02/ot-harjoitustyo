from repository.house_repository import HouseRepository as default_house_repository
from repository.transaction_repository import TransactionsRepository as default_transaction_repository
from database_connection import get_database_connection

class HouseService:
    def __init__(
        self,
        house_repository=default_house_repository(get_database_connection()),
        transaction_repository=default_transaction_repository(get_database_connection())
        ):
        self.house_repository = house_repository
        self.transaction_repository = transaction_repository
        self.setup_houses()

    def new_house(self,house_name,house_address):
        self.house_repository.create_house(house_name,house_address)

    def update_house_info(self,house_id,house_name,house_address):
        self.house_repository.edit_house_info(house_id,house_name,house_address)

    def get_houses(self):
        houses = self.house_repository.get_houses()
        return houses

    def report_of_all_houses(self):
        houses = self.houses
        report = []
        for house in houses:
            house_report = house.house_report()
            house_report['name'] = house.name
            report.append(house_report)
        # print(report)
        return report

    def setup_houses(self):
        self.houses = self.house_repository.get_houses()
        self.transactions = self.transaction_repository.get_transactions()
        ## transaction to houses
        house_dict = {}
        for house in self.houses:
            house_dict[house.id] = house
        for transaction_to_add in self.transactions:
            if transaction_to_add.transaction_type == 'income':
                house_dict[transaction_to_add.house_id].incomes.append(transaction_to_add)
            else:
                house_dict[transaction_to_add.house_id].expenses.append(transaction_to_add)

house_service = HouseService()
