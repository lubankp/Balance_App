from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd


def plot(master, data):
    # the figure that will contain the plot
    dataframe = pd.DataFrame(data)

    fig = Figure(figsize=(6, 5), dpi=100)
    plot1 = fig.add_subplot(111)
    plot1.set_ylabel('Value')
    plot1.set_xlabel('Date')
    plot1.set_title('Bank')
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas_app = FigureCanvasTkAgg(fig, master=master)
    canvas_app.draw()
    canvas_app.get_tk_widget().grid(column=1, row=0, columnspan=4)
    try:
        dataframe = dataframe[['Date', 'Bank']].groupby('Date').sum()
    except:
        dataframe = dataframe[['Date', 'Balance']].groupby('Date').sum()
    dataframe.plot(kind='line', legend=True, ax=plot1, marker='o', fontsize=10)
    # creating the Matplotlib toolbar
    toolbar_frame = Frame(master)
    toolbar_frame.grid(column=0, row=1, columnspan=4, sticky='nw')
    toolbar = NavigationToolbar2Tk(canvas_app, toolbar_frame)
    return canvas_app.get_width_height()[1] + toolbar.winfo_reqheight()
