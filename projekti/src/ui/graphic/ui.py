from tkinter import Menu, Tk
from main_view import MainView
from new_house_view import NewHouseView
from transaction_view import TransactionView
from edit_house_view import EditHouseView
from navbar import Navbar

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_navbar()
        self._show_navbar()
        self._show_main_view()
        
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
    
    def _show_navbar(self):
        self._current_view = Navbar(
            self._root,
            self._handle_main,
            self._handle_new_house,
            self._handle_transaction,
            self._handle_edit_house_info
        )
        self._current_view.pack()

    def _handle_new_house(self):
        self._show_new_house_view()

    def _handle_main(self):
        self._show_main_view()
    
    def _handle_transaction(self):
        self._show_transaction_view()
    
    def _handle_edit_house_info(self):
        self._show_edit_house_info_view()

    def _show_transaction_view(self):
        self._hide_current_view()
        
        self._current_view = TransactionView(
            self._root
        )
        self._current_view.pack()

    def _show_edit_house_info_view(self):
        self._hide_current_view()
        
        self._current_view = EditHouseView(
            self._root
        )
        self._current_view.pack()

    def _show_main_view(self):
        self._hide_current_view()

        self._current_view = MainView(
            self._root
        )

        self._current_view.pack()

    def _show_new_house_view(self):
        self._hide_current_view()

        self._current_view = NewHouseView(
            self._root
        )

        self._current_view.pack()

window = Tk()
window.title("Vuokran seuranta")

ui = UI(window)
ui.start()

window.mainloop()