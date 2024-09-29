import matplotlib.pyplot as mpl
from visualization import plot_cube
import tkinter as tk

valid_faces = ['U', 'D', 'R', 'L', 'F', 'B']
valid_colors = ['W', 'G', 'R', 'B', 'Y', 'O']
valid_row_and_column = ['R', 'C']
valid_indices = ['1' ,'2', '3']


def user_cube(cube, colors, label_state, ax, move_entry, message_label):
    message_label.config(text="Please enter the centre pieces as they appear in the cube diagram.\n\
                         Enter the face (U, D, F, B, L, R) followed by 'R' for row/'C' for column number, \
                         then the orientation of colors\n\
                         (Example: UR1WWW, DC2RGB)") 
    plot_cube(cube, colors, label_state, ax)
    face = move_entry.get().upper()
    move_entry.delete(0, tk.END) 
    if len(face) == 6 and \
        (face[0] in valid_faces and \
            face[1] in valid_row_and_column and \
            face[2] in valid_indices and \
                all(face[i + 3] in valid_colors for i in range(3))):
        if face[1] == 'R':
            row_index = int(face[2]) - 1
            for i in range(3):
                cube[face[0]][row_index, i] = face[i + 3]
        elif face[1] == 'C':
            column_index = int(face[2]) - 1
            for i in range(3):
                cube[face[0]][i, column_index] = face[i + 3]
    else:
        message_label.config(text="Invalid input. Please type a valid move.\n\
                             Please enter the centre pieces as they appear in the cube diagram.\n\
                             Enter the face (U, D, F, B, L, R) followed by 'R' for row/'C' for column number,\
                              then the orientation of colors\n\
                             (Example: UR1WWW, DC2RGB)") 

 