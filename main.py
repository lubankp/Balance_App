# Imports
import table
import main_window
import events
import database_def


# Application objects
window = main_window.MainWindow()
events = events.Events(window)
table = table.Table(window.frame_data, database_def.organize_red_data())
events.init_table(table)
window.init_buttons(events.create_record, events.refresh_data, events.delete_record, events.update_record)
events.refresh_data('init')

window.bind('<Button-1>', lambda event: events.widget_under_mouse())

window.mainloop()
