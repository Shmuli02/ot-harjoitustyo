import sys
from menu import Menu
from ui.ui import UI
from tkinter import Tk
from ui.graphic.graphic_ui import GraphicUI
from database_connection import get_database_connection
from repository.house_repository import HouseRepository
from repository.transaction_repository import TransactionsRepository


def main():
    ui = UI()
    house_repository = HouseRepository(get_database_connection())
    transaction_repository = TransactionsRepository(get_database_connection())
    menu = Menu(ui,house_repository,transaction_repository)
    menu.setup_houses()
    menu.command_line_runner()

def graphic_main():
    window = Tk()
    window.title("Vuokran seuranta")
    ui = GraphicUI(window)
    ui.start()

    window.mainloop()

if __name__ == '__main__':
    if str(sys.argv[1]) == 'commandline':
        main()
    elif str(sys.argv[1]) == 'graphic':
        graphic_main()
    else:
        pass
