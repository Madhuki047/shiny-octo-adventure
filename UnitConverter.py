# Importing python libraries (tkinter)
import tkinter as tk
from tkinter import ttk

# Manages user interface and functionality of unit converter window
class UnitConverter:
    # Initialize unit converter window
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(self.root)
        self.window.title("Unit Converter")
        self.window.configure(bg="Thistle")
        self.window.geometry("500x300")
        # Create widgets
        self.create_widgets()

    # Creates and designs user interface elements
    def create_widgets(self):
        # Define unit categories
        categories = ["Select", "Length", "Weight", "Temperature", "Angle"]
        
        # Create label & variable to hold selected category
        category_var = tk.StringVar(value="Select")
        category_label = tk.Label(self.window, text="Select Category", font=("Helvetica", 14))
        category_label.pack(pady=5)
        
        # Drop-down menu for selecting category
        category_menu = ttk.Combobox(self.window, textvariable=category_var, values=categories, state="readonly")
        category_menu.pack(pady=5)
        category_menu.bind("<<ComboboxSelected>>", lambda event: self.update_units(category_var.get()))
        
        # Variables to hold selected units & inputs
        self.unit_from_var = tk.StringVar(value="Select")
        self.unit_to_var = tk.StringVar(value="Select")
        self.entry_var = tk.StringVar(value="1")
        self.result_var = tk.StringVar(value="")

        # Frame for unit selection
        unit_frame = tk.Frame(self.window)
        unit_frame.pack(pady=5)

        # Label & dropdown for selecting 'From' unit
        self.unit_from_label = tk.Label(unit_frame, text="From", font=("Helvetica", 14))
        self.unit_from_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.unit_from_menu = ttk.Combobox(unit_frame, textvariable=self.unit_from_var, state="readonly")
        self.unit_from_menu.grid(row=1, column=0, padx=5, pady=5)
        
        # Label & dropdown for selecting 'To' unit
        self.unit_to_label = tk.Label(unit_frame, text="To", font=("Helvetica", 14))
        self.unit_to_label.grid(row=0, column=1, padx=5, pady=5)
        
        self.unit_to_menu = ttk.Combobox(unit_frame, textvariable=self.unit_to_var, state="readonly")
        self.unit_to_menu.grid(row=1, column=1, padx=5, pady=5)
        
        # Frame for entry and result
        conversion_frame = tk.Frame(self.window)
        conversion_frame.pack(pady=5)

        # Create & place lable & entry for input value
        entry_label = tk.Label(conversion_frame, text="Value", font=("Helvetica", 14))
        entry_label.grid(row=2, column=0, padx=5, pady=5)
        
        entry = tk.Entry(conversion_frame, textvariable=self.entry_var, font=("Helvetica", 14))
        entry.grid(row=3, column=0, padx=5, pady=5)
        
        # Create & place lable & entry for result value
        result_label = tk.Label(conversion_frame, text="Result", font=("Helvetica", 14))
        result_label.grid(row=2, column=1, padx=5, pady=5)
        
        result = tk.Entry(conversion_frame, textvariable=self.result_var, font=("Helvetica", 14), state="readonly")
        result.grid(row=3, column=1, padx=5, pady=5)
        
        # Button to trigger conversion
        convert_button = tk.Button(self.window, text="Convert", command=self.convert_units, font=("Helvetica", 14))
        convert_button.pack(pady=10)

    # Updates available units based on category selected by user
    def update_units(self, category):
        units = {
            "Length": ["Select", "centimeter", "meter", "kilometer", "mile", "inch"],
            "Weight": ["Select", "gram", "kilogram", "pound", "ounce"],
            "Temperature": ["Select", "celsius", "fahrenheit", "kelvin"],
            "Angle": ["Select", "degree", "radian"]
        }
        
        # Set unit selection to 'Select'
        self.unit_from_var.set("Select")
        self.unit_to_var.set("Select")
        
        # Update dropdowns for units accourding to category selected
        self.unit_from_menu["values"] = units.get(category, ["Select"])
        self.unit_to_menu["values"] = units.get(category, ["Select"])

    # Converts input value from one unit type to another
    def convert_units(self):
        # Get input value and selected units
        value = float(self.entry_var.get())
        unit_from = self.unit_from_var.get()
        unit_to = self.unit_to_var.get()
        # Check selections & perform conversion
        if unit_from == "Select" or unit_to == "Select":
            self.result_var.set("Please select units")
        else:
            result = self.perform_conversion(value, unit_from, unit_to)
            self.result_var.set(result)

    # Performs tha numerical unit conversion & returns value
    def perform_conversion(self, value, unit_from, unit_to):
        # Dictionary of unit converson formulas
        conversions = {
            ("meter", "kilometer"): value / 1000,
            ("kilometer", "meter"): value * 1000,
            ("meter", "centimeter"): value * 100,
            ("centimeter", "meter"): value / 100,
            ("meter", "mile"): value / 1609.34,
            ("mile", "meter"): value * 1609.34,
            ("meter", "inch"): value * 39.3701,
            ("inch", "meter"): value / 39.3701,
            ("kilometer", "centimeter"): value * 100000,
            ("centimeter", "kilometer"): value / 100000,
            ("kilometer", "mile"): value / 1.60934,
            ("mile", "kilometer"): value * 1.60934,
            ("kilometer", "inch"): value * 39370.1,
            ("inch", "kilometer"): value / 39370.1,
            ("centimeter", "mile"): value / 160934,
            ("mile", "centimeter"): value * 160934,
            ("centimeter", "inch"): value / 2.54,
            ("inch", "centimeter"): value * 2.54,
            ("gram", "kilogram"): value / 1000,
            ("kilogram", "gram"): value * 1000,
            ("pound", "kilogram"): value * 0.453592,
            ("kilogram", "pound"): value / 0.453592,
            ("gram", "pound"): value * 0.00220462,
            ("pound", "gram"): value / 0.00220462,
            ("ounce", "gram"): value * 28.3495,
            ("gram", "ounce"): value / 28.3495,
            ("kilogram", "ounce"): value * 35.274,
            ("ounce", "kilogram"): value / 35.274,
            ("celsius", "fahrenheit"): value * 9 / 5 + 32,
            ("fahrenheit", "celsius"): (value - 32) * 5 / 9,
            ("celsius", "kelvin"): value + 273.15,
            ("kelvin", "celsius"): value - 273.15,
            ("fahrenheit", "kelvin"): (value - 32) * 5 / 9 + 273.15,
            ("kelvin", "fahrenheit"): (value - 273.15) * 9 / 5 + 32,
            ("degree", "radian"): value * (3.141592653589793 / 180),
            ("radian", "degree"): value * (180 / 3.141592653589793),
        }

        # Return converted value or error
        return conversions.get((unit_from, unit_to), "Conversion not possible")
        # return conversions.get((unit_from, unit_to), "Error")