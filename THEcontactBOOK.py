import tkinter as tk
import ClassDatabase
import ClassGUI

class Contact:
    def __init__(self, first_name, surname, phone, email):
        self.first_name = first_name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"{self.first_name} {self.surname} - {self.phone} - {self.email}"
    
    

if __name__ == "__main__":
    db = ClassDatabase.Database()
    contact_manager = ClassDatabase.DatabaseManagement(db)
    root = tk.Tk()
    app = ClassGUI.CommandsForGUI(root, contact_manager)
    app.load_data()
    root.mainloop()