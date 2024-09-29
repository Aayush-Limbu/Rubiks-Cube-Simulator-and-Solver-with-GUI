import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from cube import Cube
from rotation import rotate_cube_clockwise, rotate_cube_anticlockwise
from visualization import plot_cube, update_cube_plot
from custom_cube import user_cube
from solve import cube_solve

class CubeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cube Solver")
        
        self.cube_instance = Cube()
        
        self.figure = Figure(figsize=(5, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack()
        
        plot_cube(self.cube_instance.cube, self.cube_instance.colors, 0, self.ax)

        self.move_entry = tk.Entry(root)
        self.move_entry.pack()
        
        self.move_button = tk.Button(root, text="Submit Move", command=self.submit_move)
        self.move_button.pack()
        
        self.solve_button = tk.Button(root, text="Solve Cube", command=self.solve_cube)
        self.solve_button.pack()
        
        self.user_cube_button = tk.Button(root, text="Enter Custom Cube", command=self.enter_custom_cube)
        self.user_cube_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()

        self.message_label = tk.Label(root, text="", fg="red")
        self.message_label.pack()

        self.solution_label = tk.Label(root, text="", fg="blue")
        self.solution_label.pack()



    def submit_move(self):
        user_input = self.move_entry.get().upper()
        self.move_entry.delete(0, tk.END) 
        
        if user_input in ['U', 'D', 'R', 'L', 'F', 'B']:
            rotate_cube_clockwise(self.cube_instance.cube, user_input)
            update_cube_plot(self.canvas, self.cube_instance.cube, self.cube_instance.colors, 0, self.ax)
            self.message_label.config(text="")  
        elif user_input in ["U'", "D'", "R'", "L'", "F'", "B'"]:
            rotate_cube_anticlockwise(self.cube_instance.cube, user_input)
            update_cube_plot(self.canvas, self.cube_instance.cube, self.cube_instance.colors, 0, self.ax)
            self.message_label.config(text="")  
        else:
            self.message_label.config(text="Invalid input. Please type a valid move.") 

    def enter_custom_cube(self):
        user_cube(self.cube_instance.cube, self.cube_instance.colors, 1, self.ax, self.move_entry, self.message_label)
        update_cube_plot(self.canvas, self.cube_instance.cube, self.cube_instance.colors, 1, self.ax)

    def solve_cube(self):
        solution = cube_solve(self.cube_instance.cube)
        self.solution_label.config(text=f"Solution: {solution}") 

    def update_message(self, message):
        self.message_label.config(text=message)
