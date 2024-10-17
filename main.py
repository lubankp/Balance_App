# Imports
import table
import database_def
import main_window
import create_window as cr
from tkinter import *

import plot

# Constants

widget = ''

# ---------------------------- Create Table ------------------------- #
def create_table():
    database_def.create_table()

# ---------------------------- Create Record  ------------------------- #
def create_record():
    create_window = cr.CreateWindow(window)
    data = create_window.get_values()
    
    database_def.create_record(data[0], data[1], data[2])
    refresh_data('create')
    create_window.destroy()

# ---------------------------- Update Record  ------------------------- #
def update_record():
    input = window.update_field.get("1.0", END)
    database_def.update_record(t.coords(widget), input)
    refresh_data('update')

# ---------------------------- Delete Record  ------------------------- #
def delete_record():

    database_def.delete_record(t.coords(widget))
    refresh_data('delete')

# ----------------------------- Plot -----------------------------------#
def read_records():
    fun_id = ['Id']
    fun_date = ['Date']
    fun_PKOSA = ['PKOSA']
    fun_Mbank = ['Mbank']
    fun_Revolut = ['Revolut']
    fun_Balance = ['Balance']

    records = database_def.read_all()
    for record in records:
        row_dict = dict(record._mapping)
        row_object = row_dict['Balance']
        fun_id.append(row_object.Id)
        fun_date.append(row_object.Date)
        fun_PKOSA.append(row_object.PKOSA)
        fun_Mbank.append(row_object.Mbank)
        fun_Revolut.append(row_object.Revolut)
        fun_Balance.append(row_object.Balance)

    return [fun_id, fun_date, fun_PKOSA, fun_Mbank, fun_Revolut, fun_Balance]


def choose_diag(bank, records):

    if bank == 'PKOSA':
        return {'Date': records[0][1:], 'Bank': records[1][1:]}
    elif bank == 'Mbank':
        return {'Date': records[0][1:], 'Bank': records[2][1:]}
    elif bank == 'Revolut':
        return {'Date': records[0][1:], 'Bank': records[3][1:]}
    else:
        return {'Date': records[0][1:], 'Balance': records[4][1:]}



def refresh_data(button):
    records = read_records()
    if button == 'update':
        t.update(records)
    elif button == 'delete' or button == 'create':
        t.delete()
        t.__init__(window.frame_data, records)
    plot_high = plot.plot(window.tab1, choose_diag('PKOSA', records[1:]))
    plot.plot(window.tab2, choose_diag('Mbank', records[1:]))
    plot.plot(window.tab3, choose_diag('Revolut', records[1:]))
    plot.plot(window.tab4, choose_diag('Balance', records[1:]))

    window.frame_canvas.config(width=t.total_columns * t.width + window.vsb.winfo_width(), height=plot_high)
    window.frame_canvas.update_idletasks()
    window.canvas.config(scrollregion=window.canvas.bbox('all'))

# ---------------------------- UI SETUP ------------------------------- #


def print_widget_under_mouse(root):
    global widget
    x,y = root.winfo_pointerxy()
    new_widget = root.winfo_containing(x,y)
    if new_widget.winfo_class() == 'Entry':
        widget = new_widget
        window.update_field.delete('1.0', END)
        window.update_field.insert(END, widget.get())
        print(widget)

# Application objects
window = main_window.MainWindow()
t = table.Table(window.frame_data, read_records())
window.init_buttons(create_record, refresh_data, delete_record, update_record)
refresh_data('init')


window.bind('<Button-1>', lambda event: print_widget_under_mouse(window))

window.mainloop()
