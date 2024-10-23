import database_def
import create_window as cr
from tkinter import *
import plot

class Events():

    def __init__(self, window):
        self.window = window
        self.widget = ''

    def init_table(self, table):
        self.table = table

    def refresh_data(self, button):
        records = database_def.organize_red_data()
        if button == 'update':
            self.table.update(records)
        elif button == 'delete' or button == 'create':
            self.table.delete()
            self.table.__init__(self.window.frame_data, records)
        plot_high = plot.plot(self.window.tab1, self.choose_diag('PKOSA', records[1:]))
        plot.plot(self.window.tab2, self.choose_diag('Mbank', records[1:]))
        plot.plot(self.window.tab3, self.choose_diag('Revolut', records[1:]))
        plot.plot(self.window.tab4, self.choose_diag('Balance', records[1:]))

        self.window.frame_canvas.config(width=self.table.total_columns * self.table.width + self.window.vsb.winfo_width(), height=plot_high)
        self.window.frame_canvas.update_idletasks()
        self.window.canvas.config(scrollregion=self.window.canvas.bbox('all'))

    # ---------------------------- Create Table ------------------------- #
    def create_table(self):
        database_def.create_table()

    # ---------------------------- Create Record  ------------------------- #
    def create_record(self):
        create_window = cr.CreateWindow(self.window)
        data = create_window.get_values()

        database_def.create_record(data[0], data[1], data[2])
        self.refresh_data('create')
        create_window.destroy()

    # ---------------------------- Update Record  ------------------------- #
    def update_record(self):
        input = self.window.update_field.get("1.0", END)
        database_def.update_record(self.table.coords(self.widget), input)
        self.refresh_data('update')

    # ---------------------------- Delete Record  ------------------------- #
    def delete_record(self):

        database_def.delete_record(self.table.coords(self.widget))
        self.refresh_data('delete')

    # ----------------------------- Choose Diagram -----------------------------------#
    def choose_diag(self, bank, records):

        if bank == 'PKOSA':
            return {'Date': records[0][1:], 'Bank': records[1][1:]}
        elif bank == 'Mbank':
            return {'Date': records[0][1:], 'Bank': records[2][1:]}
        elif bank == 'Revolut':
            return {'Date': records[0][1:], 'Bank': records[3][1:]}
        else:
            return {'Date': records[0][1:], 'Balance': records[4][1:]}

    # ----------------------------- Choose Diagram -----------------------------------#
    def widget_under_mouse(self):
        x, y = self.window.winfo_pointerxy()
        new_widget = self.window.winfo_containing(x, y)
        if new_widget.winfo_class() == 'Entry':
            self.widget = new_widget
            self.window.update_field.delete('1.0', END)
            self.window.update_field.insert(END, self.widget.get())
