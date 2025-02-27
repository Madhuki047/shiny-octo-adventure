# Importing tkinter to support GUI
import tkinter as tk
# Importing 2 supporting python files to run program
import ClassDatabase
import ClassGUI

# Defining class with attributes first_name, surname, phone and email
class Contact:
    def __init__(self, first_name, surname, phone, email):
        self.first_name = first_name
        self.surname = surname
        self.phone = phone
        self.email = email
    

if __name__ == "__main__":
    # Initializing database and contact manager
    db = ClassDatabase.Database()
    contact_manager = ClassDatabase.DatabaseManagement(db)
    # Creating main application window
    root = tk.Tk()
    # Initializing GUI with root window and contact manager
    app = ClassGUI.CommandsForGUI(root, contact_manager)
    # Loading data to GUI
    app.load_data()
    # Starts Tkinter event loop
    root.mainloop()
    