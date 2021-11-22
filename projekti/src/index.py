from menu import Menu
from ui.ui import UI
from database_connection import get_database_connection
from repository.house_repository import HouseRepository
from repository.transaction_repository import TransactionsRepository

def main():
    ui = UI()
    house_repository = HouseRepository(get_database_connection())
    transaction_repository = TransactionsRepository(get_database_connection())
    menu = Menu(ui,house_repository,transaction_repository)
    menu.command_line_runner()

if __name__ == '__main__':
    main()
