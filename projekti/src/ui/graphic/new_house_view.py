from tkinter import ttk, constants

class NewHouseView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        title_label = ttk.Label(master=self._frame, text="Uusi asunto")

        house_name_label = ttk.Label(master=self._frame, text="Asunnon nimi")
        house_name_entry = ttk.Entry(master=self._frame)

        house_address_label = ttk.Label(master=self._frame,text='Asunnon osoite')
        house_address_entry = ttk.Entry(master=self._frame)

        house_submit_button = ttk.Button(
            master=self._frame,
            text="Lisää"
        )

        title_label.grid(row=0, column=0)

        house_name_label.grid(row=2, column=0)
        house_name_entry.grid(row=2, column=1)

        house_address_label.grid(row=3, column=0)
        house_address_entry.grid(row=3, column=1)

        house_submit_button.grid(row=4, column=0, columnspan= 2)
