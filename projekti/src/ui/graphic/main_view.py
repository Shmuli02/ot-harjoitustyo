from tkinter import ttk, constants
from services.house_services import house_service

class MainView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._houses_report = house_service.report_of_all_houses()
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        if len(self._houses_report)==0:
            no_house_label = ttk.Label(master=self._frame, text="Ei asuntoja.")
            no_house_label.grid(row=1, column=0)
        else:

            heading_label = ttk.Label(master=self._frame, text="Asunto")

            income_label = ttk.Label(master=self._frame, text="Tulot: ")

            expense_label = ttk.Label(master=self._frame, text="Menot: ")

            for i in range(0,len(self._houses_report)):
                house = self._houses_report[i]
                house_name_label = ttk.Label(master=self._frame,text=house['name'])
                house_income_label = ttk.Label(master=self._frame, text=house['incomes'])
                house_expense_label = ttk.Label(master=self._frame,text=house['expenses'])
                house_name_label.grid(row=2+i,column=0)
                house_income_label.grid(row=2+i,column=1)
                house_expense_label.grid(row=2+i,column=2)


            heading_label.grid(row=1, column=0)

            income_label.grid(row=1, column=1)

            expense_label.grid(row=1, column=2)
