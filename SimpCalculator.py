import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk


class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.configure(bg="White")
        self.menu()
        
    def menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='Menu', menu=filemenu)
        filemenu.add_command(label='New', command=self.new_cal)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=root.quit)
        helpmenu = Menu(menu)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About', command=self.help_button)

    def new_cal(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Simple Calculator (New)")
        GUI(new_window)
    
    def help_button(self):
        pop_window = tk.Toplevel(self.root)
        pop_window.title("Help")
        pop_window.configure(bg="LightCyan")
        
        heading_label = tk.Label(pop_window, text="Guide to 'Simple Calculator'", font=("Comic Sans MS", 24, "bold italic"), fg="NavyBlue", bg="LightCyan")
        heading_label.pack()
        heading_label.grid(row=0, column=0, padx=10, pady=10)
        
        image = Image.open("C:\\Users\\madhu\\OneDrive\\Desktop\\University\\PS & Prog\\vscode & pycharm\\ASSESSMENT\\CalcInstructions1.png")
        photo = ImageTk.PhotoImage(image)

        # Create a Label widget to display the image
        label = tk.Label(pop_window, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
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
            
    

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    gui = GUI(root)
    root.mainloop()