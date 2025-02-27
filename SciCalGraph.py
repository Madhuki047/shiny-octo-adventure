# Importing neccessary python libraries
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Manages user interface and functionality of trigonometry graph window
class ScientificCal:
    # Initialize trig graph plotting window
    def __init__(self, root):
        self.root = root
        self.canvas = None
        self.x_data = np.array([])
        self.y_data = np.array([])

    # Creates and designs the user interface and window
    def sci_cal(self):
        self.scientific_window = tk.Toplevel(self.root)
        self.scientific_window.title("Trigonometry Graphs")
        self.scientific_window.geometry("480x650")
        self.scientific_window.configure(bg="Lavender")

        # Options for trigonometric functions
        options = ['Select Function', 'Sin', 'Cos', 'Tan', 'Sinh', 'Cosh', 'Tanh']
        self.selected_option = tk.StringVar(self.scientific_window)
        self.selected_option.set(options[0])

        # Drop-down options menu
        option_menu = ttk.Combobox(self.scientific_window, textvariable=self.selected_option, values=options, state='readonly')
        option_menu.pack(pady=10)

        # Radiobuttons for selecting degrees or radians for the graph & coordinates
        self.unit = tk.StringVar(value="Degrees")
        tk.Radiobutton(self.scientific_window, text="Degrees", variable=self.unit, value="Degrees", bg="White", command=self.update_entries).pack(anchor=tk.W)
        tk.Radiobutton(self.scientific_window, text="Radians", variable=self.unit, value="Radians", bg="White", command=self.update_entries).pack(anchor=tk.W)

        # Create & place frame, label & entry fields for x-axis range inputs
        x_range_frame = tk.Frame(self.scientific_window, bg="White")
        x_range_frame.pack(pady=10)

        x_label = tk.Label(x_range_frame, text="X-axis range:", bg="White")
        x_label.pack(side=tk.LEFT, padx=5)

        self.x_min_entry = tk.Entry(x_range_frame, width=10)
        self.x_min_entry.pack(side=tk.LEFT, padx=5)
        self.x_min_entry.insert(0, "-360")

        self.x_max_entry = tk.Entry(x_range_frame, width=10)
        self.x_max_entry.pack(side=tk.LEFT, padx=5)
        self.x_max_entry.insert(0, "360")

        # Create & place frame, label & entry fields for y-axis range inputs
        y_range_frame = tk.Frame(self.scientific_window, bg="White")
        y_range_frame.pack(pady=10)

        y_label = tk.Label(y_range_frame, text="Y-axis range:", bg="White")
        y_label.pack(side=tk.LEFT, padx=5)

        self.y_min_entry = tk.Entry(y_range_frame, width=10)
        self.y_min_entry.pack(side=tk.LEFT, padx=5)
        self.y_min_entry.insert(0, "-1")

        self.y_max_entry = tk.Entry(y_range_frame, width=10)
        self.y_max_entry.pack(side=tk.LEFT, padx=5)
        self.y_max_entry.insert(0, "1")

        # Create & place frame, label and entry fields to input specific coordinate values
        point_input_frame = tk.Frame(self.scientific_window, bg="White")
        point_input_frame.pack(pady=10)

        x_value_label = tk.Label(point_input_frame, text="X value:", bg="White")
        x_value_label.pack(side=tk.LEFT, padx=5)

        self.x_value_entry = tk.Entry(point_input_frame, width=15)
        self.x_value_entry.pack(side=tk.LEFT, padx=5)

        y_value_label = tk.Label(point_input_frame, text="Y value:", bg="White")
        y_value_label.pack(side=tk.LEFT, padx=5)

        self.y_value_entry = tk.Entry(point_input_frame, width=15)
        self.y_value_entry.pack(side=tk.LEFT, padx=5)

        # Create & place get coordinate and plot buttons
        get_coordinate_button = tk.Button(point_input_frame, text="Get Coordinate", command=self.get_coordinate)
        get_coordinate_button.pack(side=tk.LEFT, padx=5)

        plot_button = tk.Button(self.scientific_window, text="Plot", command=self.plot_graph)
        plot_button.pack(pady=10)

    # Updates x-axis range values according to the units used(deg/rad)
    def update_entries(self):
        try:
            # Get values from entry fields as floats
            x_min = float(self.x_min_entry.get())
            x_max = float(self.x_max_entry.get())
            # Convert values based on unit selection
            if self.unit.get() == "Degrees":
                x_min = np.rad2deg(x_min)
                x_max = np.rad2deg(x_max)
            else:
                x_min = np.deg2rad(x_min)
                x_max = np.deg2rad(x_max)
            # Update entry fields with converted values
            self.x_min_entry.delete(0, tk.END)
            self.x_min_entry.insert(0, str(x_min))
            self.x_max_entry.delete(0, tk.END)
            self.x_max_entry.insert(0, str(x_max))
        except ValueError:
            pass

    # Plots graph of the selected trigonometric function
    def plot_graph(self):
        selected_function = self.selected_option.get()
        # Show error if no function is selected
        if selected_function == 'Select Function':
            messagebox.showerror("Error", "Please select a function to plot.")
            return

        try:
            # Get axis range values from entry fields
            x_min = float(self.x_min_entry.get())
            x_max = float(self.x_max_entry.get())
            y_min = float(self.y_min_entry.get())
            y_max = float(self.y_max_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for the axis ranges.")
            return

        # Generate x values between x_min & x_max
        x = np.linspace(x_min, x_max, 1000)
        if self.unit.get() == "Degrees":
            x_rad = np.deg2rad(x)  # Convert degrees to radians for trigonometric functions
        else:
            x_rad = x              # Use radians directly

        # Initialize y values to zero
        y = np.zeros_like(x)
        # Compute y values based on selected function
        if selected_function == 'Sin':
            y = np.sin(x_rad)
        elif selected_function == 'Cos':
            y = np.cos(x_rad)
        elif selected_function == 'Tan':
            y = np.tan(x_rad)
            y[np.abs(y) > 10] = np.nan       # Hide large values to better show asymptotes
        elif selected_function == 'Sinh':
            y = np.sinh(x_rad)
        elif selected_function == 'Cosh':
            y = np.cosh(x_rad)
        elif selected_function == 'Tanh':
            y = np.tanh(x_rad)

        self.x_data = x
        self.y_data = y

        # Create a new figure and plot data
        fig, ax = plt.subplots()
        ax.plot(x, y, label=selected_function)
        if selected_function == 'Tan':
            # Add vertical asymptotes for tan
            for k in range(int(np.floor(x_min / 180)), int(np.ceil(x_max / 180))):
                asymptote = (k + 0.5) * 180
                ax.axvline(x=asymptote, color='red', linestyle='--')

        ax.legend()
        ax.set_ylim([y_min, y_max])  # Set y-axis limits
        ax.set_xlim([x_min, x_max])  # Set x-axis limits

        # Clear the previous plot if it exists
        if self.canvas:
            self.canvas.get_tk_widget().pack_forget()

        # Embed the plot in the scientific_window
        self.canvas = FigureCanvasTkAgg(fig, master=self.scientific_window)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        # Bind the click event
        self.canvas.mpl_connect("button_press_event", self.on_click)

    # Handles click event on graph to display co-ordinates
    def on_click(self, event):
        if event.inaxes is not None:
            x_clicked = event.xdata
            y_clicked = event.ydata
            print(f"Clicked coordinates: x={x_clicked}, y={y_clicked}")
            messagebox.showinfo("Coordinates", f"Clicked coordinates: x={x_clicked:.2f}, y={y_clicked:.2f}")
        else:
            print("Clicked outside the plot area")

    # Provides respective x/y co-ordinate for a give x/y co-ordinate
    def get_coordinate(self):
        x_value = self.x_value_entry.get()  # Get the x value from the entry field
        y_value = self.y_value_entry.get()  # Get the y value from the entry field

        # Check if the graph has been plotted
        if self.x_data.size == 0 or self.y_data.size == 0:
            messagebox.showerror("Error", "Please plot the graph before getting coordinates.")
            return

        # Ensure at least one coordinate value (x or y) is provided
        if not x_value and not y_value:
            messagebox.showerror("Error", "Please provide at least one coordinate value (x or y).")
            return

        try:
            if x_value and not y_value:
                x_value = float(x_value)         # Converts x value to float
                # Degrees
                if self.unit.get() == "Degrees":
                    if -360 <= x_value <= 360:  # Check if x value is within acceptable range for degrees
                        selected_function = self.selected_option.get()
                        # Calculate corresponding y value based on selected function
                        if selected_function == 'Sin':
                            y_value = np.sin(np.deg2rad(x_value))
                        elif selected_function == 'Cos':
                            y_value = np.cos(np.deg2rad(x_value))
                        elif selected_function == 'Tan':
                            y_value = np.tan(np.deg2rad(x_value))
                        elif selected_function == 'Sinh':
                            y_value = np.sinh(np.deg2rad(x_value))
                        elif selected_function == 'Cosh':
                            y_value = np.cosh(np.deg2rad(x_value))
                        elif selected_function == 'Tanh':
                            y_value = np.tanh(np.deg2rad(x_value))
                        # Show co-ordinates in messagebox
                        messagebox.showinfo("Coordinate", f"For x={x_value:.2f} degrees, y={y_value:.2f}")
                    else:
                        raise ValueError("X value out of range")
                # Radians
                else:
                    if -2 * np.pi <= x_value <= 2 * np.pi:  # Check if x value is within acceptable range for radians
                        selected_function = self.selected_option.get()
                        # Calculate corresponding y value based on selected function
                        if selected_function == 'Sin':
                            y_value = np.sin(x_value)
                        elif selected_function == 'Cos':
                            y_value = np.cos(x_value)
                        elif selected_function == 'Tan':
                            y_value = np.tan(x_value)
                        elif selected_function == 'Sinh':
                            y_value = np.sinh(x_value)
                        elif selected_function == 'Cosh':
                            y_value = np.cosh(x_value)
                        elif selected_function == 'Tanh':
                            y_value = np.tanh(x_value)
                        # Show co-ordinates in messagebox
                        messagebox.showinfo("Coordinate", f"For x={x_value:.2f} radians, y={y_value:.2f}")
                    else:
                        raise ValueError("X value out of range")
            elif y_value and not x_value:
                y_value = float(y_value)  # Converts y value to float
                # Degrees
                if self.unit.get() == "Degrees":
                    selected_function = self.selected_option.get()
                    x_value = None
                    # Calculate corresponding x value based on selected function
                    if selected_function == 'Sin':
                        x_value = np.rad2deg(np.arcsin(y_value))
                    elif selected_function == 'Cos':
                        x_value = np.rad2deg(np.arccos(y_value))
                    elif selected_function == 'Tan':
                        x_value = np.rad2deg(np.arctan(y_value))
                    elif selected_function == 'Sinh':
                        x_value = np.rad2deg(np.arcsinh(y_value))
                    elif selected_function == 'Cosh':
                        if y_value >= 1:
                            x_value = np.rad2deg(np.arccosh(y_value))
                        else:
                            raise ValueError("Y value out of range for Cosh")
                    elif selected_function == 'Tanh':
                        if np.abs(y_value) < 1:
                            x_value = np.rad2deg(np.arctanh(y_value))
                        else:
                            raise ValueError("Y value out of range for Tanh")

                    if x_value is not None:
                        # Show co-ordinates in messagebox
                        messagebox.showinfo("Coordinate", f"For y={y_value:.2f}, x={x_value:.2f} degrees")
                    else:
                        raise ValueError("No valid x values found for the given y value")
                # Radians
                else:  
                    selected_function = self.selected_option.get()
                    x_value = None
                    # Calculate corresponding x value based on selected function
                    if selected_function == 'Sin':
                        x_value = np.arcsin(y_value)
                    elif selected_function == 'Cos':
                        x_value = np.arccos(y_value)
                    elif selected_function == 'Tan':
                        x_value = np.arctan(y_value)
                    elif selected_function == 'Sinh':
                        x_value = np.arcsinh(y_value)
                    elif selected_function == 'Cosh':
                        if y_value >= 1:
                            x_value = np.arccosh(y_value)
                        else:
                            raise ValueError("Y value out of range for Cosh")
                    elif selected_function == 'Tanh':
                        if np.abs(y_value) < 1:
                            x_value = np.arctanh(y_value)
                        else:
                            raise ValueError("Y value out of range for Tanh")
                    
                    if x_value is not None:
                        # Show co-ordinates in messagebox
                        messagebox.showinfo("Coordinate", f"For y={y_value:.2f}, x={x_value:.2f} radians")
                    else:
                        raise ValueError("No valid x values found for the given y value")
            else:
                messagebox.showerror("Error", "Please provide one valid coordinate value (x or y).")
        except ValueError as e:
            messagebox.showerror("Error", f"Please ensure graph is plotted and valid x or y coordinate is provided. {str(e)}")
