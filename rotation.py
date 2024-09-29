import numpy as np

def rotate_cube_clockwise(cube, face):
    if face == 'U':
        cube['F'][0, :], cube['L'][0, :], cube['B'][0, :], cube['R'][0, :] = \
            cube['R'][0, :].copy(), cube['F'][0, :].copy(), cube['L'][0, :].copy(), cube['B'][0, :].copy()

    elif face == 'D':
        cube['F'][2, :], cube['L'][2, :], cube['B'][2, :], cube['R'][2, :] = \
            cube['L'][2, :].copy(), cube['B'][2, :].copy(), cube['R'][2, :].copy(), cube['F'][2, :].copy()

    elif face == 'R':
        cube['F'][:, 2], cube['U'][:, 2], cube['B'][::-1, 0], cube['D'][::-1, 2] = \
            cube['D'][:, 2].copy(), cube['F'][:, 2].copy(), cube['U'][:, 2].copy(), cube['B'][:, 0].copy()

    elif face == 'L':
        cube['F'][:, 0], cube['U'][:, 0], cube['B'][:, 2], cube['D'][:, 0] = \
            cube['U'][:, 0].copy(), cube['B'][::-1, 2].copy(), cube['D'][::-1, 0].copy(), cube['F'][:, 0].copy()

    elif face == 'F':
        cube['L'][:, 2], cube['U'][2, ::-1], cube['R'][:, 0], cube['D'][0, ::-1] = \
            cube['D'][0, :].copy(), cube['L'][:, 2].copy(), cube['U'][2, :].copy(), cube['R'][:, 0].copy()        

    elif face == 'B':
        cube['L'][:, 0], cube['U'][0, :], cube['R'][:, 2], cube['D'][2, ::-1] = \
            cube['U'][0, ::-1].copy(), cube['R'][:, 2].copy(), cube['D'][2, ::-1].copy(), cube['L'][::-1, 0].copy()

    cube[face] = np.rot90(cube[face], -1)

        
def rotate_cube_anticlockwise(cube, face):
    if face == 'U\'':
        cube['F'][0, :], cube['L'][0, :], cube['B'][0, :], cube['R'][0, :] = \
            cube['L'][0, :].copy(), cube['B'][0, :].copy(), cube['R'][0, :].copy(), cube['F'][0, :].copy()
        
    elif face == 'D\'':
        cube['F'][2, :], cube['L'][2, :], cube['B'][2, :], cube['R'][2, :] = \
            cube['R'][2, :].copy(), cube['F'][2, :].copy(), cube['L'][2, :].copy(), cube['B'][2, :].copy()
        
        
    elif face == 'R\'':
        cube['F'][:, 2], cube['U'][:, 2], cube['B'][:, 0], cube['D'][:, 2] = \
            cube['U'][:, 2].copy(), cube['B'][::-1, 0].copy(), cube['D'][::-1, 2].copy(), cube['F'][:, 2].copy()
        
    elif face == 'L\'':
        cube['F'][:, 0], cube['U'][:, 0], cube['B'][:, 2], cube['D'][:, 0] = \
            cube['D'][:, 0].copy(), cube['F'][:, 0].copy(), cube['U'][::-1, 0].copy(), cube['B'][::-1, 2].copy()

    elif face == 'F\'':
        cube['L'][:, 2], cube['U'][2, :], cube['R'][::-1, 0], cube['D'][0, :] = \
            cube['U'][2, ::-1].copy(), cube['R'][:, 0].copy(), cube['D'][0, :].copy(), cube['L'][:, 2].copy() 
        
    elif face == 'B\'':
        cube['L'][:, 0], cube['U'][0, ::-1], cube['R'][::-1, 2], cube['D'][2, ::-1] = \
            cube['D'][2, :].copy(), cube['L'][:, 0].copy(), cube['U'][0, ::-1].copy(), cube['R'][:, 2].copy()
        
    cube[face[0]] = np.rot90(cube[face[0]], 1)