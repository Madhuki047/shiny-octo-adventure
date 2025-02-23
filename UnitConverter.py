import tkinter as tk
from tkinter import ttk

class UnitConverter:
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(self.root)
        self.window.title("Unit Converter")
        self.window.configure(bg="Thistle")
        self.create_widgets()

    def create_widgets(self):
        categories = ["Select", "Length", "Weight", "Temperature", "Angle"]
        
        category_var = tk.StringVar(value="Select")
        category_label = tk.Label(self.window, text="Select Category", font=("Helvetica", 14))
        category_label.pack(pady=5)
        
        category_menu = ttk.Combobox(self.window, textvariable=category_var, values=categories, state="readonly")
        category_menu.pack(pady=5)
        category_menu.bind("<<ComboboxSelected>>", lambda event: self.update_units(category_var.get()))
        
        self.unit_from_var = tk.StringVar(value="Select")
        self.unit_to_var = tk.StringVar(value="Select")
        self.entry_var = tk.StringVar(value="1")
        self.result_var = tk.StringVar(value="")

        # Frame for unit selection
        unit_frame = tk.Frame(self.window)
        unit_frame.pack(pady=5)

        self.unit_from_label = tk.Label(unit_frame, text="From", font=("Helvetica", 14))
        self.unit_from_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.unit_from_menu = ttk.Combobox(unit_frame, textvariable=self.unit_from_var, state="readonly")
        self.unit_from_menu.grid(row=1, column=0, padx=5, pady=5)
        
        self.unit_to_label = tk.Label(unit_frame, text="To", font=("Helvetica", 14))
        self.unit_to_label.grid(row=0, column=1, padx=5, pady=5)
        
        self.unit_to_menu = ttk.Combobox(unit_frame, textvariable=self.unit_to_var, state="readonly")
        self.unit_to_menu.grid(row=1, column=1, padx=5, pady=5)
        
        # Frame for entry and result
        conversion_frame = tk.Frame(self.window)
        conversion_frame.pack(pady=5)

        entry_label = tk.Label(conversion_frame, text="Value", font=("Helvetica", 14))
        entry_label.grid(row=2, column=0, padx=5, pady=5)
        
        entry = tk.Entry(conversion_frame, textvariable=self.entry_var, font=("Helvetica", 14))
        entry.grid(row=3, column=0, padx=5, pady=5)
        
        result_label = tk.Label(conversion_frame, text="Result", font=("Helvetica", 14))
        result_label.grid(row=2, column=1, padx=5, pady=5)
        
        result = tk.Entry(conversion_frame, textvariable=self.result_var, font=("Helvetica", 14), state="readonly")
        result.grid(row=3, column=1, padx=5, pady=5)
        
        convert_button = tk.Button(self.window, text="Convert", command=self.convert_units, font=("Helvetica", 14))
        convert_button.pack(pady=10)

    def update_units(self, category):
        units = {
            "Length": ["Select", "meter", "kilometer", "mile", "inch"],
            "Weight": ["Select", "gram", "kilogram", "pound", "ounce"],
            "Temperature": ["Select", "celsius", "fahrenheit", "kelvin"],
            "Angle": ["Select", "degree", "radian"]
        }
        
        self.unit_from_var.set("Select")
        self.unit_to_var.set("Select")
        
        self.unit_from_menu["values"] = units.get(category, ["Select"])
        self.unit_to_menu["values"] = units.get(category, ["Select"])

    def convert_units(self):
        value = float(self.entry_var.get())
        unit_from = self.unit_from_var.get()
        unit_to = self.unit_to_var.get()
        if unit_from == "Select" or unit_to == "Select":
            self.result_var.set("Please select units")
        else:
            result = self.perform_conversion(value, unit_from, unit_to)
            self.result_var.set(result)

    def perform_conversion(self, value, unit_from, unit_to):
        conversions = {
            ("meter", "kilometer"): value / 1000,
            ("kilometer", "meter"): value * 1000,
            ("mile", "kilometer"): value * 1.60934,
            ("kilometer", "mile"): value / 1.60934,
            ("gram", "kilogram"): value / 1000,
            ("kilogram", "gram"): value * 1000,
            ("pound", "kilogram"): value * 0.453592,
            ("kilogram", "pound"): value / 0.453592,
            ("celsius", "fahrenheit"): value * 9/5 + 32,
            ("fahrenheit", "celsius"): (value - 32) * 5/9,
            ("celsius", "kelvin"): value + 273.15,
            ("kelvin", "celsius"): value - 273.15,
            ("degree", "radian"): value * (3.141592653589793 / 180),
            ("radian", "degree"): value * (180 / 3.141592653589793),
            # Add more conversions as needed
        }
        
        return conversions.get((unit_from, unit_to), "Error")
