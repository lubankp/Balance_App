# Imports libraries
from tkinter import *
from tkinter.ttk import Notebook

class MainWindow(Tk):
    """Creates GUI"""

    BACKGROUND_COLOR = "#B1DDC6"

    def __init__(self):
        super().__init__("Balance Application")
        # Init Main Window
        # self.title()
        self.config(padx=10, pady=10, bg=self.BACKGROUND_COLOR)
        self.init_main_frame()
        self.init_canvas_frame()
        self.init_canvas()
        self.init_scrollbar()
        self.init_data_frame()
        self.init_tab_control()
        self.init_update_field()

    def init_main_frame(self):
        """Init Main Frame"""

        self.main_frame = Frame(self, width=700, height=600)
        self.main_frame.grid(sticky='news')
        self.main_frame.config(bg=self.BACKGROUND_COLOR)

    def init_canvas_frame(self):
        """Init Frame Canvas"""

        self.frame_canvas = Frame(self.main_frame, width=700, height=600)
        self.frame_canvas.grid(row=0, column=0, pady=(5, 0), sticky='nw')
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 buttons resizing later
        self.frame_canvas.grid_propagate(False)

    def init_canvas(self):
        """Adds a canvas in that Frame Canvas"""

        self.canvas = Canvas(self.frame_canvas, bg="yellow")
        self.canvas.grid(row=0, column=0, sticky="news")

    def init_scrollbar(self):
        """Links a scrollbar to the canvas"""

        self.vsb = Scrollbar(self.frame_canvas, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.canvas.config(yscrollcommand=self.vsb.set)

    def init_data_frame(self):
        """Creates a frame to contain the Entries"""

        self.frame_data = Frame(self.canvas, bg=self.BACKGROUND_COLOR)
        self.canvas.create_window((0, 0), window=self.frame_data, anchor='nw')

    def init_tab_control(self):
        """Creates Tab Controls"""

        self.tabControl = Notebook(self.main_frame)
        self.tab1 = Frame(self.tabControl)
        self.tab2 = Frame(self.tabControl)
        self.tab3 = Frame(self.tabControl)
        self.tab4 = Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='PKOSA')
        self.tabControl.add(self.tab2, text='Mbank')
        self.tabControl.add(self.tab3, text='Revolut')
        self.tabControl.add(self.tab4, text='Balance')
        self.tabControl.grid(column=1, row=0, columnspan=4)

    def init_buttons(self, create_record, refresh_data, delete_record, update_record, migration):
        """Creates all buttons"""

        # Create record button
        button_create_record = Button(self.main_frame, text='Create Record', highlightthickness=0, bg='white',
                                      command=create_record)
        button_create_record.grid(row=1, column=1, padx=0, pady=10)

        # Refresh button
        button_refresh = Button(self.main_frame, text='Refresh', highlightthickness=0, bg='white',
                                command=refresh_data)
        button_refresh.grid(row=1, column=2, padx=0, pady=10)

        # Delete record button
        button_delete_record = Button(self.main_frame, text='Delete Record', highlightthickness=0, bg='white',
                                      command=delete_record)
        button_delete_record.grid(row=1, column=3, padx=0, pady=10)

        # Update record button
        button_update = Button(self.main_frame, text='Update', highlightthickness=0, bg='white',
                               command=update_record)
        button_update.grid(row=3, column=0, padx=0, pady=10)

        # Migrate button
        button_migrate = Button(self.main_frame, text='Migrate', highlightthickness=0, bg='white',
                                command=migration)
        button_migrate.grid(row=1, column=4, padx=0, pady=10)

    def init_update_field(self):
        """Creates Field to update data"""

        self.update_field = Text(self.main_frame, fg='black', width=90, height=3, font=('Arial', 10, 'bold'), bg='white')
        self.update_field.grid(row=1, column=0, padx=0, pady=10, rowspan=2)
