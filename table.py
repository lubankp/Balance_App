from tkinter import *
import numpy

class Table:

    def __init__(self, root, list):

        self.total_rows = len(list[0])
        self.total_columns = len(list)
        self.width = 0
        self.height = 0
        self.e = [[Entry(root, fg='black', width=20, font=('Arial', 10, 'bold'), bg="#B1DDC6") for j in range(self.total_columns)] for i in range(self.total_rows)]


        # code for creating table
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                self.e[i][j].grid(row=i, column=j)
                self.e[i][j].insert(END, list[j][i])
                self.height = self.e[i][j].winfo_reqheight()
                self.width = self.e[i][j].winfo_reqwidth()


    def update(self, list):
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                self.e[i][j].delete(0, 'end')
                self.e[i][j].insert(END, list[j][i])

    def coords(self, widget):
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                if self.e[i][j] == widget:
                    return [self.e[i][0].get(), self.e[0][j].get()]
