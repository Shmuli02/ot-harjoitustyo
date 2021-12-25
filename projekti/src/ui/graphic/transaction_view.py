from tkinter import ttk, constants
from services.house_services import house_service
from services.transaction_services import transaction_service

class TransactionView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._houses = house_service.get_houses()
        self._categories = transaction_service.get_categories()
        self._amount_entey = None
        self._house_entry = None
        self._description_entry = None
        self._category_entry = None
        self._transaction_type_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_new_transaction(self):
        if self._transaction_type_entry.get() == 'Tulo':
            transaction_type = 'income'
        else:
            transaction_type = 'expense'
        house = [house.id for house in self._houses if house.name == self._house_entry.get()][0]
        category = [category['category_id'] for category in self._categories if category['category'] == self._category_entry.get()][0]
        amount = self._amount_entey.get()
        description = self._description_entry.get()
        transaction_service.add_transaction(house,category,amount,description,transaction_type)
        house_service.setup_houses()


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        new_transaction_label = ttk.Label(master=self._frame,text="Uusi tapahtuma")

        transaction_type_label = ttk.Label(master=self._frame, text='Meno/Tulo')
        self._transaction_type_entry = ttk.Combobox(master=self._frame, values=['Tulo','Meno'])

        house_label = ttk.Label(master=self._frame, text="Asunto")
        self._house_entry= ttk.Combobox(master=self._frame,
            values=[house.name for house in self._houses])

        amount_label = ttk.Label(master=self._frame, text="Summma")
        self._amount_entey= ttk.Entry(master=self._frame)

        category_label = ttk.Label(master=self._frame, text="Kategoria")
        self._category_entry = ttk.Combobox(master=self._frame,
            values=[category['category'] for category in self._categories])

        description_label = ttk.Label(master=self._frame, text="Selite")
        self._description_entry = ttk.Entry(master=self._frame)

        transaction_submit_button = ttk.Button(
            master=self._frame,
            text="Lisää",
            command=self._handle_new_transaction
        )

        new_transaction_label.grid(row=1,column=0)

        transaction_type_label.grid(row=2, column=0)
        self._transaction_type_entry.grid(row=2, column=1)
        house_label.grid(row=3,column=0)
        self._house_entry.grid(row=3, column=1)
        category_label.grid(row=4, column=0)
        self._category_entry.grid(row=4, column=1)
        amount_label.grid(row=5, column=0)
        self._amount_entey.grid(row=5, column=1)
        description_label.grid(row=6, column=0)
        self._description_entry.grid(row=6, column=1)
        transaction_submit_button.grid(row=7, column=0, columnspan=2)
