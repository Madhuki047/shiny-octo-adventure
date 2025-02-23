import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
import SciCalGraph
import UnitConverter
import math
import re

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("312x465")
        self.root.configure(bg="White")
        self.scientific_calculator = SciCalGraph.ScientificCal(self.root)
        self.menu()

    def menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='Menu', menu=filemenu)
        filemenu.add_command(label='New', command=self.new_cal)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.root.quit)

        science_menu = Menu(menu)
        menu.add_cascade(label='Scientific', menu=science_menu)
        science_menu.add_command(label='Trig Graphs', command=self.scientific_calculator.sci_cal)  # Renamed option
        science_menu.add_command(label='Scientific Calculator', command=self.open_scientific_calculator)  # New option

        helpmenu = Menu(menu)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About', command=self.help_button)

    def new_cal(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Simple Calculator (New)")
        GUI(new_window)

    def open_scientific_calculator(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Scientific Calculator")
        new_window.geometry('620x450')
        new_window.configure(bg="LightBlue")
        ScientificCalculator(new_window)

    def help_button(self):
        pop_window = tk.Toplevel(self.root)
        pop_window.title("Help")
        pop_window.configure(bg="LightCyan")

        heading_label = tk.Label(pop_window, text="Guide to 'Simple Calculator'", font=("Comic Sans MS", 24, "bold italic"), fg="NavyBlue", bg="LightCyan")
        heading_label.pack()
        heading_label.grid(row=0, column=0, padx=10, pady=10)

        image = Image.open("C:\\Users\\madhu\\OneDrive\\Desktop\\University\\PS & Prog\\vscode & pycharm\\ASSESSMENT\\CalcInstructions1.png")
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(pop_window, image=photo)
        label.image = photo
        label.grid(row=1, column=0, padx=10, pady=10)

class GUI:
    def __init__(self, root):
        self.root = root
        self.screen_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        screen = tk.Entry(self.root, text=self.screen_var, font=("Arial", 20, "bold"), fg="Teal", bg="LightCyan")
        screen.pack(fill=tk.BOTH, pady=10, padx=10)

        button_frame = tk.Frame(self.root, bg="White")
        button_frame.pack()

        button_texts = [
            ('C', 0, 0, 16, 15, 'Orange'), ('(', 0, 1, 20, 15, 'LightSkyBlue'), (')', 0, 2, 20, 15, 'LightSkyBlue'), ('AC', 0, 3, 10, 15, 'tomato'),
            ('7', 1, 0, 17, 15, 'LightBlue'), ('8', 1, 1, 17, 15, 'LightBlue'), ('9', 1, 2, 17, 15, 'LightBlue'), ('*', 1, 3, 18.5, 15, 'PeachPuff'),
            ('4', 2, 0, 17, 15, 'LightBlue'), ('5', 2, 1, 17, 15, 'LightBlue'), ('6', 2, 2, 17, 15, 'LightBlue'), ('-', 2, 3, 19.5, 15, 'PeachPuff'),
            ('1', 3, 0, 17, 15, 'LightBlue'), ('2', 3, 1, 17, 15, 'LightBlue'), ('3', 3, 2, 17, 15, 'LightBlue'), ('+', 3, 3, 17, 15, 'PeachPuff'),
            ('=', 4, 0, 17, 15, 'MediumSeaGreen'), ('0', 4, 1, 17, 15, 'LightBlue'), ('.', 4, 2, 20, 15, 'LightSkyBlue'), ('/', 4, 3, 20, 15, 'PeachPuff')
        ]


        for (text, row, col, ipadx, ipady, color) in button_texts:
            button = tk.Button(button_frame, text=text, font=("Helvetica", 14, "bold"), fg="DarkBlue", padx=5, pady=5, bg=color)
            button.grid(row=row, column=col, padx=2, pady=2, ipadx=ipadx, ipady=ipady)
            button.bind("<Button-1>", self.click)

    def click(self, event):
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = str(eval(self.screen_var.get()))
                self.screen_var.set(result)
            except Exception as e:
                self.screen_var.set("Error")
                self.root.after(1000, lambda: self.screen_var.set(""))
        elif text == "AC":
            self.screen_var.set("")
        elif text == "C":
            current_text = self.screen_var.get()
            self.screen_var.set(current_text[:-1])
        else:
            self.screen_var.set(self.screen_var.get() + text)


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.screen_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        screen = tk.Entry(self.root, text=self.screen_var, font=("Arial", 20, "bold"), fg="Teal", bg="LightCyan")
        screen.pack(fill=tk.BOTH, pady=10, padx=10)

        button_frame = tk.Frame(self.root, bg="PowderBlue")
        button_frame.pack()

        button_texts = [
            ('(', 0, 0, 'LightSkyBlue', 2, 6, 1), (')', 0, 1, 'LightSkyBlue', 2, 6, 1), ('C', 0, 2, 'LightCoral', 2, 6, 1), ('AC', 0, 3, 'IndianRed', 2, 6, 1), ('log', 0, 4, 'MediumOrchid', 2, 6, 1), ('ln', 0, 5, 'MediumOrchid', 2, 6, 1), ('exp', 0, 6, 'DarkOrchid', 2, 6, 1),
            ('7', 1, 0, 'LightSteelBlue', 2, 6, 1), ('8', 1, 1, 'LightSteelBlue', 2, 6, 1), ('9', 1, 2, 'LightSteelBlue', 2, 6, 1), ('/', 1, 3, 'MediumTurquoise', 2, 6, 1), ('sin', 1, 4, 'LightSkyBlue', 2, 6, 1), ('cos', 1, 5, 'LightSkyBlue', 2, 6, 1), ('tan', 1, 6, 'LightSkyBlue', 2, 6, 1),
            ('4', 2, 0, 'LightSteelBlue', 2, 6, 1), ('5', 2, 1, 'LightSteelBlue', 2, 6, 1), ('6', 2, 2, 'LightSteelBlue', 2, 6, 1), ('*', 2, 3, 'MediumTurquoise', 2, 6, 1), ('arcsin', 2, 4, 'LightSkyBlue', 2, 6, 1), ('arccos', 2, 5, 'LightSkyBlue', 2, 6, 1), ('arctan', 2, 6, 'LightSkyBlue', 2, 6, 1),
            ('1', 3, 0, 'LightSteelBlue', 2, 6, 1), ('2', 3, 1, 'LightSteelBlue', 2, 6, 1), ('3', 3, 2, 'LightSteelBlue', 2, 6, 1), ('-', 3, 3, 'MediumTurquoise', 2, 6, 1), ('sinh', 3, 4, 'MediumSeaGreen', 2, 6, 1), ('cosh', 3, 5, 'MediumSeaGreen', 2, 6, 1), ('tanh', 3, 6, 'MediumSeaGreen', 2, 6, 1),
            ('.', 4, 0, 'SlateGray', 2, 6, 1), ('0', 4, 1, 'LightSteelBlue', 2, 6, 1), ('=', 4, 2, 'SpringGreen', 2, 6, 1), ('+', 4, 3, 'MediumTurquoise', 2, 6, 1), ('arcsinh', 4, 4, 'MediumSeaGreen', 2, 6, 1), ('arccosh', 4, 5, 'MediumSeaGreen', 2, 6, 1), ('arctanh', 4, 6, 'MediumSeaGreen', 2, 6, 1),
            ('%', 5, 0, 'SteelBlue', 2, 6, 1), ('^', 5, 1, 'SteelBlue', 2, 6, 1), ('√', 5, 2, 'SteelBlue', 2, 6, 1), ('π', 5, 3, 'Gold', 2, 6, 1), ('e', 5, 4, 'Gold', 2, 6, 1), ('Unit Converter', 5, 5, 'Orchid', 2, 14, 2)
        ]

        for (text, row, col, color, height, width, columnspan) in button_texts:
            button = tk.Button(button_frame, text=text, font=("Helvetica", 14, "bold"), fg="DarkBlue", bg=color, height=height, width=width)
            button.grid(row=row, column=col, padx=2, pady=2, columnspan=columnspan)
            button.bind("<Button-1>", self.click)

   

    def evaluate_expression(self, expression):
        functions = {
            'sin': 'math.sin', 'cos': 'math.cos', 'tan': 'math.tan',
            'arcsin': 'math.asin', 'arccos': 'math.acos', 'arctan': 'math.atan',
            'sinh': 'math.sinh', 'cosh': 'math.cosh', 'tanh': 'math.tanh',
            'arcsinh': 'math.asinh', 'arccosh': 'math.acosh', 'arctanh': 'math.atanh',
            'log': 'math.log10', 'ln': 'math.log',
            '^': '**', 'π': 'math.pi', 'e': 'math.e'
        }

        if '%' in expression:
            expression = re.sub(r'(\d+)%', r'(\1*0.01)', expression)

        for key in functions.keys():
            expression = re.sub(r'\b' + re.escape(key) + r'\b', f"__{key}__", expression)

        for key, value in functions.items():
            expression = expression.replace(f"__{key}__", value)

        expression = expression.replace('√', 'math.sqrt(')
        expression = expression.replace('exp', '*10**')
        
        expression = re.sub(r'(?<!\d|\))\*10\*\*', '1*10**', expression)
        expression = re.sub(r'\*10\*\*(?!\d|\()', '*10**0', expression)
         
        try:
            result = eval(expression, {"math": math})
            if isinstance(result, float):
                result = round(result, 20)
                if abs(result) < 1e-10:
                    result = 0.0
            return result
        except Exception as e:
            print("Error", e)
            return "Error"


    def click(self, event):
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = str(self.evaluate_expression(self.screen_var.get()))
                self.screen_var.set(result)
            except Exception as e:
                self.screen_var.set("Error")
                self.root.after(1000, lambda: self.screen_var.set(""))
        elif text == "AC":
            self.screen_var.set("")
        elif text == "C":
            current_text = self.screen_var.get()
            self.screen_var.set(current_text[:-1])
        elif text == "Unit Converter":
            UnitConverter.UnitConverter(self.root)
        else:
            self.screen_var.set(self.screen_var.get() + text)



if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    gui = GUI(root)
    root.mainloop()