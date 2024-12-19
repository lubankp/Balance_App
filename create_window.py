# Imports libraries
from tkinter import *

class CreateWindow(Toplevel):
    """Creates Toplevel window"""

    def __init__(self, window):
        super().__init__(window)

        # sets the title of the
        self.title("Set Record")
        # sets the geometry of toplevel
        self.geometry("300x300")
        self.init_labels()
        self.init_entries()
        self.init_button()

    def init_labels(self):
        """A Label widget to show in Toplevel"""

        Title = Label(self, text="Set values", fg="black").grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        Label_PKOSA = Label(self, text="PKO SA", fg="black").grid(row=2, column=1, padx=10, pady=10)
        Label_Mbank = Label(self, text="Mbank", fg="black").grid(row=3, column=1, padx=10, pady=10)
        Label_Revolut = Label(self, text="Revolut", fg="black").grid(row=4, column=1, padx=10, pady=10)

    def init_entries(self):
        """Creates Entries in Toplevel"""
        self.entry_pkosa = Entry(self, text="", textvariable=DoubleVar())
        self.entry_pkosa.grid(row=2, column=2)
        self.entry_mbank = Entry(self, text="", textvariable=DoubleVar())
        self.entry_mbank.grid(row=3, column=2)
        self.entry_revolut = Entry(self, text="", textvariable=DoubleVar())
        self.entry_revolut.grid(row=4, column=2)

    def init_button(self):
        """Creates buttons in Toplevel"""
        self.button_pressed = StringVar()
        self.button = Button(self, text="Save", command=lambda: self.button_pressed.set("button pressed"))
        self.button.grid(row=5, columnspan=2)

    def get_values(self):
        """Catch values set in Entries"""
        self.button.wait_variable(self.button_pressed)
        entry1 = float(self.entry_pkosa.get())
        entry2 = float(self.entry_mbank.get())
        entry3 = float(self.entry_revolut.get())
        return [entry1, entry2, entry3]