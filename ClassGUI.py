import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import THEcontactBOOK



class ContactsMainGUI:
    def __init__(self, root, contact_manager):
        self.root = root
        self.contact_manager = contact_manager
        self.root.title("Contact Book")
        self.root.geometry("800x600")
        
        image = Image.open("C:\\Users\\madhu\\OneDrive\\Desktop\\University\\PS & Prog\\vscode & pycharm\\ASSESSMENT\\ContactImage1.jpg")
        photo = ImageTk.PhotoImage(image)
        
        # Create a Label widget to display the image
        label = tk.Label(root, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack()
        
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Contact Book", font=("Comic Sans MS", 24, "bold italic"), fg="Salmon")
        self.label.place(relx=0.5, rely=0.01, anchor="n")
        
        self.search_frame = tk.Frame(self.root, bd=5, bg="MistyRose")
        self.search_frame.place(relx=0.5, rely=0.11, relwidth=0.52, relheight=0.06, anchor='n')

        self.search_label = tk.Label(self.search_frame, font=("Arial", 10), text="Search:")
        self.search_label.place(relx=0.01, rely=0.11, anchor="nw")

        self.search_entry = tk.Entry(self.search_frame, font=("Arial", 10))
        self.search_entry.place(relx=0.2, rely=0.11)
        
        self.search_button = tk.Button(self.search_frame, text="Search", bg="MediumVioletRed", fg="whitesmoke", font=("Arial", 9, "bold"), command=self.search_contacts)
        self.search_button.place(relx=0.74, rely=0.5, anchor="e")

        self.clear_search_button = tk.Button(self.search_frame, text="Clear Search", bg="DarkViolet", fg="whitesmoke", font=("Arial", 9, "bold"), command=self.clear_search)
        self.clear_search_button.place(relx=0.99, rely=0.5, anchor="e")


        self.tree_frame = tk.Frame(self.root, bg='PeachPuff', bd=7)
        self.tree_frame.place(relx=0.5, rely=0.21, relwidth=0.75, relheight=0.45, anchor='n')
        
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", background="Pink", font=("Comic Sans MS", 11, "italic"), foreground="DarkBlue")

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

        scrollbar_ver = ttk.Scrollbar(self.tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar_ver.set)
        scrollbar_ver.pack(side=tk.RIGHT, fill=tk.Y)

        self.add_button = tk.Button(self.root, font=("Arial", 10), text="Add Contact", bg="#A8E6CF", command=self.show_add_contact_fields)
        self.add_button.place(relx=0.27, rely=0.7)

        self.edit_button = tk.Button(self.root, font=("Arial", 10), text="Edit Contact", bg="#E6E6FA", command=self.show_edit_contact_fields)
        self.edit_button.place(relx=0.44, rely=0.7)

        self.delete_button = tk.Button(self.root, font=("Arial", 10), text="Delete Contact", bg="Tomato", command=self.delete_contact_gui)
        self.delete_button.place(relx=0.6, rely=0.7)

        self.quit_button = tk.Button(self.root, font=("Arial", 10), text="Quit", bg="#8B0000", fg="white", command=self.root.quit)
        self.quit_button.place(relx=0.38, rely=0.8, relwidth=0.2)






class CommandsForGUI(ContactsMainGUI):
    def __init__(self, root, contact_manager):
        super().__init__(root, contact_manager)

    def show_add_contact_fields(self):
        self.add_contact_window = tk.Toplevel(self.root)
        self.add_contact_window.title("Add Contact")
        self.add_contact_window.geometry("300x215")
        self.add_contact_window.configure(bg="#A8E6CF")

        self.first_name_label = tk.Label(self.add_contact_window, bg="#A8E6CF", font=("Arial", 10, "bold"), text="First Name")
        self.first_name_label.grid(row=0, column=0, pady=5, padx=7)
        self.first_name_entry = tk.Entry(self.add_contact_window)
        self.first_name_entry.grid(row=0, column=1, pady=5)

        self.surname_label = tk.Label(self.add_contact_window, bg="#A8E6CF", font=("Arial", 10, "bold"), text="Surname")
        self.surname_label.grid(row=1, column=0, pady=5, padx=7)
        self.surname_entry = tk.Entry(self.add_contact_window)
        self.surname_entry.grid(row=1, column=1, pady=5)

        self.phone_label = tk.Label(self.add_contact_window, bg="#A8E6CF", font=("Arial", 10, "bold"), text="Phone")
        self.phone_label.grid(row=2, column=0, pady=5, padx=7)
        self.phone_entry = tk.Entry(self.add_contact_window)
        self.phone_entry.grid(row=2, column=1, pady=5)

        self.email_label = tk.Label(self.add_contact_window, bg="#A8E6CF", font=("Arial", 10, "bold"), text="Email")
        self.email_label.grid(row=3, column=0, pady=5, padx=7)
        self.email_entry = tk.Entry(self.add_contact_window)
        self.email_entry.grid(row=3, column=1, pady=5)

        self.save_button = tk.Button(self.add_contact_window, bg="#20B2AA", text="Save Contact", font=("Arial", 10, "bold"), command=self.add_contact_gui)
        self.save_button.grid(row=4, column=0, padx=20, pady=10)

        self.clear_button = tk.Button(self.add_contact_window, bg="#EEE8AA", text="Clear Fields", font=("Arial", 10, "bold"), command=self.clear_fields)
        self.clear_button.grid(row=4, column=1, padx=20, pady=10)

    def add_contact_gui(self):
        first_name = self.first_name_entry.get()
        surname = self.surname_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if (first_name == "" and surname == "") or (phone == "" and email == ""):
            messagebox.showwarning("Input Error", "Please enter a name and at least one of phone or email")
        else:
            contact = THEcontactBOOK.Contact(first_name, surname, phone, email)
            self.contact_manager.add_contact(contact)
            messagebox.showinfo("Completed", f"Contact {first_name or surname} added successfully.")
            self.clear_fields()
            self.load_data()
            self.add_contact_window.destroy()

    def show_edit_contact_fields(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a contact to update")
            return

        values = self.tree.item(selected_item, "values")
        self.selected_contact_id = values[0]

        self.edit_contact_window = tk.Toplevel(self.root)
        self.edit_contact_window.title("Update Contact")
        self.edit_contact_window.geometry("270x200")
        self.edit_contact_window.configure(bg="#E6E6FA")

        self.first_name_label = tk.Label(self.edit_contact_window, bg="#E6E6FA", font=("Arial", 10, "bold"), text="First Name")
        self.first_name_label.grid(row=0, column=0, pady=7, padx=7)
        self.first_name_entry = tk.Entry(self.edit_contact_window)
        self.first_name_entry.grid(row=0, column=1, columnspan=2, pady=5)
        self.first_name_entry.insert(0, values[1])

        self.surname_label = tk.Label(self.edit_contact_window, bg="#E6E6FA", font=("Arial", 10, "bold"), text="Surname")
        self.surname_label.grid(row=1, column=0, pady=5, padx=7)
        self.surname_entry = tk.Entry(self.edit_contact_window)
        self.surname_entry.grid(row=1, column=1, columnspan=2, pady=5)
        self.surname_entry.insert(0, values[2])

        self.phone_label = tk.Label(self.edit_contact_window, bg="#E6E6FA", font=("Arial", 10, "bold"), text="Phone")
        self.phone_label.grid(row=2, column=0, pady=5, padx=7)
        self.phone_entry = tk.Entry(self.edit_contact_window)
        self.phone_entry.grid(row=2, column=1, columnspan=2, pady=5)
        self.phone_entry.insert(0, values[3])

        self.email_label = tk.Label(self.edit_contact_window, bg="#E6E6FA", font=("Arial", 10, "bold"), text="Email")
        self.email_label.grid(row=3, column=0, pady=5, padx=7)
        self.email_entry = tk.Entry(self.edit_contact_window)
        self.email_entry.grid(row=3, column=1, columnspan=2, pady=5)
        self.email_entry.insert(0, values[4])

        self.save_button = tk.Button(self.edit_contact_window, bg="LightSteelBlue", text="Save Changes", font=("Arial", 10, "bold"), command=self.edit_contact)
        self.save_button.grid(row=4, column=1, pady=10)

        self.current_contact = THEcontactBOOK.Contact(values[1], values[2], values[3], values[4])

    def edit_contact(self):
        first_name = self.first_name_entry.get()
        surname = self.surname_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if first_name == "" and surname == "" and phone == "" and email == "":
            messagebox.showerror("Input Error", "Please enter data to be updated")
        else:
            self.current_contact.first_name = first_name
            self.current_contact.surname = surname
            self.current_contact.phone = phone
            self.current_contact.email = email
            self.contact_manager.update_contact(self.current_contact, self.selected_contact_id)
            messagebox.showinfo("Success", f"Contact {first_name or surname} updated successfully.")
            self.clear_fields()
            self.load_data()
            self.edit_contact_window.destroy()

    def delete_contact_gui(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a contact to delete")
            return

        values = self.tree.item(selected_item, "values")
        first_name = values[1]
        surname = values[2]
        phone = values[3]
        email = values[4]

        self.contact_manager.delete_contact(first_name, surname, phone, email)
        messagebox.showinfo("Completed", f"Contact {first_name} {surname} deleted successfully.")
        self.load_data()


    def load_data(self):
        self.tree.delete(*self.tree.get_children())
        rows = self.contact_manager.view_contacts()
        for row in rows:
            self.tree.insert("", "end", values=row)

    def search_contacts(self):
        query = self.search_entry.get().lower()
        self.tree.delete(*self.tree.get_children())
        rows = self.contact_manager.view_contacts()
        for row in rows:
            if query in row[1].lower() or query in row[2].lower() or query in row[3].lower() or query in row[4].lower():
                self.tree.insert("", "end", values=row)

    def clear_search(self):
        self.search_entry.delete(0, tk.END)
        self.load_data()
        
    def clear_fields(self):
        self.first_name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)