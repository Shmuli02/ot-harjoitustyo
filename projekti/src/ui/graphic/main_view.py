import tkinter as tk
from tkinter import ttk, constants

class MainView:
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

        heading_label = ttk.Label(master=self._frame, text="Tietoja")

        income_label = ttk.Label(master=self._frame, text="Tulot: ")

        expense_label = ttk.Label(master=self._frame, text="Menot: ")

        heading_label.grid(row=1, column=0)

        income_label.grid(row=2, column=0)

        expense_label.grid(row=3, column=0)
