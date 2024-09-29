import numpy as np

class Cube:
    def __init__(self):
        self.colors = {
            'W': 'white',
            'R': 'red',
            'B': 'blue',
            'Y': 'yellow',
            'G': 'green',
            'O': 'orange',
        }
        self.cube = self.create_solved_cube()

    def create_solved_cube(self):
        return {
            'U': np.full((3, 3), 'Y'),
            'F': np.full((3, 3), 'R'),
            'R': np.full((3, 3), 'G'),
            'B': np.full((3, 3), 'O'),
            'L': np.full((3, 3), 'B'),
            'D': np.full((3, 3), 'W')
        }
    
        
