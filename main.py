# Imports
import table
import database_def
from tkinter import *
from tkinter.ttk import Notebook
import plot


# Constants
BACKGROUND_COLOR = "#B1DDC6"
widget = ''

# ---------------------------- Create Table ------------------------- #
def create_table():
    database_def.create_table()

# ---------------------------- Create Record  ------------------------- #
def create_record():
    data = openNewWindow()
    #newWindow.destroy()
    database_def.create_record(data[0], data[1], data[2])
    refresh_data('create')

# ---------------------------- Update Record  ------------------------- #
def update_record():
    input = update_field.get("1.0", END)
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


def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)
    # sets the title of the
    # Toplevel widget
    newWindow.title("Set Record")
    # sets the geometry of toplevel
    newWindow.geometry("300x300")

    Title = Label(newWindow, text="Set values", fg="black").grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    # A Label widget to show in toplevel
    entry_pkosa = Entry(newWindow, text="", textvariable=DoubleVar())
    entry_pkosa.grid(row=2, column=2)
    Label1 = Label(newWindow, text="PKO SA", fg="black").grid(row=2, column=1, padx=10, pady=10)

    entry_mbank = Entry(newWindow, text="", textvariable=DoubleVar())
    entry_mbank.grid(row=3, column=2)
    Label2 = Label(newWindow, text="Mbank", fg="black").grid(row=3, column=1, padx=10, pady=10)

    entry_revolut = Entry(newWindow, text="", textvariable=DoubleVar())
    entry_revolut.grid(row=4, column=2)
    Label3 = Label(newWindow, text="Revolut", fg="black").grid(row=4, column=1, padx=10, pady=10)

    button_pressed = StringVar()
    button = Button(newWindow, text="Save", command=lambda: button_pressed.set("button pressed"))
    button.grid(row=5, columnspan=2)
    button.wait_variable(button_pressed)

    entry1 = float(entry_pkosa.get())
    entry2 = float(entry_mbank.get())
    entry3 = float(entry_revolut.get())

    return [entry1, entry2, entry3]

def refresh_data(button):
    records = read_records()
    if button == 'update':
        t.update(records)
    elif button == 'delete' or button == 'create':
        t.delete()
        t.__init__(window.frame_data, records)
    plot_high = plot.plot(tab1, choose_diag('PKOSA', records[1:]))
    plot.plot(tab2, choose_diag('Mbank', records[1:]))
    plot.plot(tab3, choose_diag('Revolut', records[1:]))
    plot.plot(tab4, choose_diag('Balance', records[1:]))

    window.frame_canvas.config(width=t.total_columns * t.width + window.vsb.winfo_width(), height=plot_high)
    window.frame_canvas.update_idletasks()
    window.canvas.config(scrollregion=window.canvas.bbox('all'))

# ---------------------------- UI SETUP ------------------------------- #
class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        self.main_frame = Frame(self, width=700, height=600)
        self.main_frame.grid(sticky='news')
        self.main_frame.config(bg=BACKGROUND_COLOR)

        self.frame_canvas = Frame(self.main_frame, width=700, height=600)
        self.frame_canvas.grid(row=0, column=0, pady=(5, 0), sticky='nw')
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        self.frame_canvas.grid_propagate(False)

        # Add a canvas in that frame
        self.canvas = Canvas(self.frame_canvas, bg="yellow")
        self.canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the canvas
        self.vsb = Scrollbar(self.frame_canvas, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.canvas.config(yscrollcommand=self.vsb.set)

        # Create a frame to contain the buttons
        self.frame_data = Frame(self.canvas, bg=BACKGROUND_COLOR)
        self.canvas.create_window((0, 0), window=self.frame_data, anchor='nw')

def print_widget_under_mouse(root):
    global widget
    x,y = root.winfo_pointerxy()
    new_widget = root.winfo_containing(x,y)
    if new_widget.winfo_class() == 'Entry':
        widget = new_widget
        update_field.delete('1.0', END)
        update_field.insert(END, widget.get())
        print(widget)


window = MainWindow()

window.title("Balance Application")
window.config(padx=10, pady=10, bg=BACKGROUND_COLOR)
tabControl = Notebook(window.main_frame)

tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tab3 = Frame(tabControl)
tab4 = Frame(tabControl)

tabControl.add(tab1, text='PKOSA')
tabControl.add(tab2, text='Mbank')
tabControl.add(tab3, text='Revolut')
tabControl.add(tab4, text='Balance')
tabControl.grid(column=1, row=0, columnspan=4)

t = table.Table(window.frame_data, read_records())

refresh_data('init')

# Create record button
button_create_record = Button(window.main_frame, text='Create Record', highlightthickness=0, bg='white', command=create_record)
button_create_record.grid(row=1, column=1, padx=0, pady=10)

# Refresh button
button_refresh = Button(window.main_frame, text='Refresh', highlightthickness=0, bg='white', command=refresh_data('refresh'))
button_refresh.grid(row=1, column=2, padx=0, pady=10)

# Delete record button
button_delete_record = Button(window.main_frame, text='Delete Record', highlightthickness=0, bg='white', command=delete_record)
button_delete_record.grid(row=1, column=3, padx=0, pady=10)

# Update record button
button_update = Button(window.main_frame, text='Update', highlightthickness=0, bg='white', command=update_record)
button_update.grid(row=3, column=0, padx=0, pady=10)

#Migrate button
button_migrate = Button(window.main_frame, text='Migrate', highlightthickness=0, bg='white', command=update_record)
button_migrate.grid(row=1, column=4, padx=0, pady=10)


#Field to update
update_field = Text(window.main_frame, fg='black', width=90, height=3, font=('Arial', 10, 'bold'), bg='white')
update_field.grid(row=1, column=0, padx=0, pady=10, rowspan=2)


window.bind('<Button-1>', lambda event: print_widget_under_mouse(window))

window.mainloop()
