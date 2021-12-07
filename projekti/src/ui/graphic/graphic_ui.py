from .main_view import MainView
from .new_house_view import NewHouseView
from .transaction_view import TransactionView
from .navbar import Navbar

class GraphicUI:
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
            self._handle_transaction        )
        self._current_view.pack()

    def _handle_new_house(self):
        self._show_new_house_view()

    def _handle_main(self):
        self._show_main_view()

    def _handle_transaction(self):
        self._show_transaction_view()

    def _show_transaction_view(self):
        self._hide_current_view()

        self._current_view = TransactionView(
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
