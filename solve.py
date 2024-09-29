from rubik_solver import utils

def cube_to_string(cube):
    
    cube_str = ""
    cube_str += ''.join(cube['U'].flatten())  
    cube_str += ''.join(cube['L'].flatten())  
    cube_str += ''.join(cube['F'].flatten())  
    cube_str += ''.join(cube['R'].flatten()) 
    cube_str += ''.join(cube['B'].flatten())  
    cube_str += ''.join(cube['D'].flatten()) 
    return cube_str.upper()

def cube_solve(cube):
    try:
        cube_str = cube_to_string(cube)
        solution = utils.solve(cube_str, 'Kociemba')
        return solution

    except Exception as e:
        return e

