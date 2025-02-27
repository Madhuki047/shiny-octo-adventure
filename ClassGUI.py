# Improting neccessary python libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
# Importing 'THEcontactBOOK' file to access attributes
import THEcontactBOOK


# Manages the layout/design of the Contact Book's main GUI
class ContactsMainGUI:
    # Initializes main window (including window's appearance)
    def __init__(self, root, contact_manager, photo=None):
        self.root = root
        self.contact_manager = contact_manager

        # Loads default photo if none provided
        if photo is None:
            image_path = "C:\\Users\\madhu\\OneDrive\\Desktop\\University\\PS & Prog\\vscode & pycharm\\ASSESSMENT\\ContactImage1.jpg"
            self.image = Image.open(image_path)
            self.photo = ImageTk.PhotoImage(self.image)
        else:
            self.photo=photo
        
        # Create a Label widget to display the image
        self.label = tk.Label(root, image=self.photo)
        self.label.image = photo  # Keep a reference to avoid garbage collection
        self.label.pack()
        
        self.root.title("Contact Book")
        self.root.geometry("800x600")     
           
        self.create_widgets()                  # Creates GUI elements
        self.load_data()                       # Load data to GUI

    # Creates the user interface elements
    def create_widgets(self):
        # Create & place window title
        self.label = tk.Label(self.root, text="Contact Book", font=("Comic Sans MS", 24, "bold italic"), fg="Salmon")
        self.label.place(relx=0.5, rely=0.01, anchor="n")
        
        # Create & place frame for search bar
        self.search_frame = tk.Frame(self.root, bd=5, bg="MistyRose")
        self.search_frame.place(relx=0.5, rely=0.11, relwidth=0.52, relheight=0.06, anchor='n')

        # Create & place search bar label
        self.search_label = tk.Label(self.search_frame, font=("Arial", 10), text="Search:")
        self.search_label.place(relx=0.01, rely=0.11, anchor="nw")

        # Create & place entry field for search bar
        self.search_entry = tk.Entry(self.search_frame, font=("Arial", 10))
        self.search_entry.place(relx=0.2, rely=0.11)
        
        # Create & place search button
        self.search_button = tk.Button(self.search_frame, text="Search", bg="MediumVioletRed", fg="whitesmoke", font=("Arial", 9, "bold"), command=self.search_contacts)
        self.search_button.place(relx=0.74, rely=0.5, anchor="e")

        # Create & place clear search button
        self.clear_search_button = tk.Button(self.search_frame, text="Clear Search", bg="DarkViolet", fg="whitesmoke", font=("Arial", 9, "bold"), command=self.clear_search)
        self.clear_search_button.place(relx=0.99, rely=0.5, anchor="e")

        # Create & place frame for treeview table (to display contacts)
        self.tree_frame = tk.Frame(self.root, bg='PeachPuff', bd=7)
        self.tree_frame.place(relx=0.5, rely=0.21, relwidth=0.75, relheight=0.45, anchor='n')
        
        # Configure treeview style
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", background="Pink", font=("Comic Sans MS", 11, "italic"), foreground="DarkBlue")

        # Create treeview table
        self.tree = ttk.Treeview(self.tree_frame, columns=("ID", "First Name", "Surname", "Phone", "Email"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("First Name", text="First Name")
        self.tree.heading("Surname", text="Surname")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.column("ID", width=50)
        self.tree.column("First Name", width=100)
        self.tree.column("Surname", width=100)
        self.tree.column("Phone", width=100)
        self.tree.column("Email", width=180)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Create vertical scrollbar for treeview
        scrollbar_ver = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar_ver.set)
        scrollbar_ver.pack(side=tk.RIGHT, fill=tk.Y)

        # Create & place Add contact button
        self.add_button = tk.Button(self.root, font=("Arial", 10), text="Add Contact", bg="#A8E6CF", command=self.show_add_contact_fields)
        self.add_button.place(relx=0.27, rely=0.7)

        # Create & place Edit contact button
        self.edit_button = tk.Button(self.root, font=("Arial", 10), text="Edit Contact", bg="#E6E6FA", command=self.show_edit_contact_fields)
        self.edit_button.place(relx=0.44, rely=0.7)

        # Create & place Delete contact button
        self.delete_button = tk.Button(self.root, font=("Arial", 10), text="Delete Contact", bg="Tomato", command=self.delete_contact_gui)
        self.delete_button.place(relx=0.6, rely=0.7)

        # Create & place quit application button
        self.quit_button = tk.Button(self.root, font=("Arial", 10), text="Quit", bg="#8B0000", fg="white", command=self.root.quit)
        self.quit_button.place(relx=0.38, rely=0.8, relwidth=0.2)


# Maages functionality of the GUI
class CommandsForGUI(ContactsMainGUI):
    # Inherits characteristics from parent class 'ContactsMainGUI'
    def __init__(self, root, contact_manager):
        super().__init__(root, contact_manager)

    # Displays new window for adding contacts
    def show_add_contact_fields(self):
        # Create new window
        self.add_contact_window = tk.Toplevel(self.root)
        self.add_contact_window.title("Add Contact")
        self.add_contact_window.geometry("300x215")
        self.add_contact_window.configure(bg="#A8E6CF")

        # Create & place entry field & label for first name
        self.first_name_label = tk.Label(self.add_contact_window, bg="#A8E6CF", font=("Arial", 10, "bold"), text="First Name")
        self.first_name_label.grid(row=0, column=0, pady=5, padx=7)
        self.first_name_entry = tk.Entry(self.add_contact_window)
        self.first_name_entry.grid(row=0, column=1, pady=5)

        # Create & place entry field & label for surname
        self.surname_label = tk.Label(self.add_contact_window, bg="#A8E6CF", font=("Arial", 10, "bold"), text="Surname")
        self.surname_label.grid(row=1, column=0, pady=5, padx=7)
        self.surname_entry = tk.Entry(self.add_contact_window)
        self.surname_entry.grid(row=1, column=1, pady=5)

        # Create & place entry field & label for phone number
        self.phone_label = tk.Label(self.add_contact_window, bg="#A8E6CF", font=("Arial", 10, "bold"), text="Phone")
        self.phone_label.grid(row=2, column=0, pady=5, padx=7)
        self.phone_entry = tk.Entry(self.add_contact_window)
        self.phone_entry.grid(row=2, column=1, pady=5)

        # Create & place entry field & label for email address
        self.email_label = tk.Label(self.add_contact_window, bg="#A8E6CF", font=("Arial", 10, "bold"), text="Email")
        self.email_label.grid(row=3, column=0, pady=5, padx=7)
        self.email_entry = tk.Entry(self.add_contact_window)
        self.email_entry.grid(row=3, column=1, pady=5)

        # Create & place save button
        self.save_button = tk.Button(self.add_contact_window, bg="#20B2AA", text="Save Contact", font=("Arial", 10, "bold"), command=self.add_contact_gui)
        self.save_button.grid(row=4, column=0, padx=20, pady=10)

        # Create & place clear fields button
        self.clear_button = tk.Button(self.add_contact_window, bg="#EEE8AA", text="Clear Fields", font=("Arial", 10, "bold"), command=self.clear_fields)
        self.clear_button.grid(row=4, column=1, padx=20, pady=10)

    # Adds new contact to add_contact of contact_manager
    def add_contact_gui(self):
        # Get details from entry fields
        first_name = self.first_name_entry.get()
        surname = self.surname_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        
        # Validate inputs - show error as needed 
        if (first_name == "" and surname == "") or (phone == "" and email == ""):
            messagebox.showwarning("Input Error", "Please enter a name and at least one of phone or email")
        else:
            if phone != "" and not phone.isdigit():
                messagebox.showwarning("Input Error", "Please enter a valid phone number")
            elif email != "" and "@" not in email:
                messagebox.showwarning("Input Error", "Please enter a valid email address")
            else:
                # Create new contact and add to contact manager
                contact = THEcontactBOOK.Contact(first_name, surname, phone, email)
                self.contact_manager.add_contact(contact)
                messagebox.showinfo("Completed", f"Contact {first_name or surname} added successfully.")
                self.clear_fields()                 # Clear fields
                self.load_data()                    # Reload data to treeview with update
                self.add_contact_window.destroy()   # Close 'add contact' window

    # Displays new window for editing contacts
    def show_edit_contact_fields(self):
        # Get selected item from treeview
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a contact to update")
            return

        # Get selected contact's details
        values = self.tree.item(selected_item, "values")
        self.selected_contact_id = values[0]

        # Create new window for editing contact
        self.edit_contact_window = tk.Toplevel(self.root)
        self.edit_contact_window.title("Update Contact")
        self.edit_contact_window.geometry("270x200")
        self.edit_contact_window.configure(bg="#E6E6FA")

        # Create & place entry field & label for first name
        self.first_name_label = tk.Label(self.edit_contact_window, bg="#E6E6FA", font=("Arial", 10, "bold"), text="First Name")
        self.first_name_label.grid(row=0, column=0, pady=7, padx=7)
        self.first_name_entry = tk.Entry(self.edit_contact_window)
        self.first_name_entry.grid(row=0, column=1, columnspan=2, pady=5)
        self.first_name_entry.insert(0, values[1])

        # Create & place entry field & label for surname
        self.surname_label = tk.Label(self.edit_contact_window, bg="#E6E6FA", font=("Arial", 10, "bold"), text="Surname")
        self.surname_label.grid(row=1, column=0, pady=5, padx=7)
        self.surname_entry = tk.Entry(self.edit_contact_window)
        self.surname_entry.grid(row=1, column=1, columnspan=2, pady=5)
        self.surname_entry.insert(0, values[2])

        # Create & place entry field & label for phone number
        self.phone_label = tk.Label(self.edit_contact_window, bg="#E6E6FA", font=("Arial", 10, "bold"), text="Phone")
        self.phone_label.grid(row=2, column=0, pady=5, padx=7)
        self.phone_entry = tk.Entry(self.edit_contact_window)
        self.phone_entry.grid(row=2, column=1, columnspan=2, pady=5)
        self.phone_entry.insert(0, values[3])

        # Create & place entry field & label for email address
        self.email_label = tk.Label(self.edit_contact_window, bg="#E6E6FA", font=("Arial", 10, "bold"), text="Email")
        self.email_label.grid(row=3, column=0, pady=5, padx=7)
        self.email_entry = tk.Entry(self.edit_contact_window)
        self.email_entry.grid(row=3, column=1, columnspan=2, pady=5)
        self.email_entry.insert(0, values[4])

        # Create & place save button
        self.save_button = tk.Button(self.edit_contact_window, bg="LightSteelBlue", text="Save Changes", font=("Arial", 10, "bold"), command=self.edit_contact)
        self.save_button.grid(row=4, column=1, pady=10)

        # Create contact object with provided values
        self.current_contact = THEcontactBOOK.Contact(values[1], values[2], values[3], values[4])

    # Updates contact informtaion in contact manager
    def edit_contact(self):
        # Get input values
        first_name = self.first_name_entry.get()
        surname = self.surname_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        # Checking input validity and raising errors accordingly
        if first_name == "" and surname == "" and phone == "" and email == "":
            messagebox.showerror("Input Error", "Please enter data to be updated")
        else:
            if phone != "" and not phone.isdigit():
                messagebox.showwarning("Input Error", "Please enter a valid phone number")
            elif email != "" and "@" not in email:
                messagebox.showwarning("Input Error", "Please enter a valid email address")
            else:
                # Updating fields
                self.current_contact.first_name = first_name
                self.current_contact.surname = surname
                self.current_contact.phone = phone
                self.current_contact.email = email
                # Saving changes to contact manager
                self.contact_manager.update_contact(self.current_contact, self.selected_contact_id)
                messagebox.showinfo("Success", f"Contact {first_name or surname} updated successfully.")
                self.clear_fields()                      # Clearing entry fields
                self.load_data()                         # Reloading data to treeview
                self.edit_contact_window.destroy()       # Closing edit contact window

    # Deletes selected contact
    def delete_contact_gui(self):
        # Getting contact selected from treeview
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a contact to delete")
            return

        # Getting selected contact's details
        values = self.tree.item(selected_item, "values")
        first_name = values[1]
        surname = values[2]
        phone = values[3]
        email = values[4]

        # Delete contact from contact manager
        self.contact_manager.delete_contact(first_name, surname, phone, email)
        messagebox.showinfo("Completed", f"Contact {first_name} {surname} deleted successfully.")
        self.load_data()            # Reloads data to treeview

    # Function to load all contacts from contact manager to treeview
    def load_data(self):
        # Clear treeview
        self.tree.delete(*self.tree.get_children())
        # Load all contacts from contact manager
        rows = self.contact_manager.view_contacts()
        for row in rows:
            self.tree.insert("", "end", values=row)

    # Search contacts based on user input
    def search_contacts(self):
        query = self.search_entry.get().lower()
        self.tree.delete(*self.tree.get_children())
        rows = self.contact_manager.view_contacts()
        for row in rows:
            if query in row[1].lower() or query in row[2].lower() or query in row[3].lower() or query in row[4].lower():
                self.tree.insert("", "end", values=row)

    # Clear search field and display all contacts in tree view
    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.load_data()
        
    # Clears input fields
    def clear_fields(self):
        self.first_name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
