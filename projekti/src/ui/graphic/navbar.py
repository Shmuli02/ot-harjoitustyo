from tkinter import ttk, constants

class Navbar:
    def __init__(self, root,handle_main,handle_new_house,handle_transactions,handle_edit_house_info):
        self._root = root
        self._handle_main = handle_main
        self._handle_new_house = handle_new_house
        self._handle_transactions = handle_transactions
        self._handle_edit_house_info = handle_edit_house_info
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        menu_button = ttk.Button(
            master=self._frame,
            text="Etusivu",
            command=self._handle_main
        )

        new_house_button = ttk.Button(
            master=self._frame,
            text="Uusi asunto",
            command=self._handle_new_house
        )

        transaction_menu_button = ttk.Button(
            master=self._frame,
            text="Tulot/Menot",
            command=self._handle_transactions
        )

        edit_house_info_button = ttk.Button(
            master=self._frame,
            text="Muokkaa asunon tietoja",
            command=self._handle_edit_house_info
        )

        menu_button.grid(row=0, column=0)
        new_house_button.grid(row=0, column=1)
        transaction_menu_button.grid(row=0, column=2)
        edit_house_info_button.grid(row=0, column=3)
