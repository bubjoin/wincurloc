# text 3d cube rotation

import wincurloc as wcl
import time
import math
import copy

cube = []
wcl.W, wcl.H = 160, 50
camera_pos = [wcl.W/2, wcl.H/2, -7]
fov_fac = 100

xs = [-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75]
ys = [-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75]
zs = [-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75]

for x in xs:
    for y in ys:
        for z in zs:
            cube.append([x, y, z])


# update
def get_cube_z_rotation(cube, rotation):
    cube_temp = copy.deepcopy(cube)
    for point in cube_temp:
        point_0 = copy.copy(point[0])
        point_1 = copy.copy(point[1])
        point[0] = (point_0*math.cos(rotation)) - (point_1*math.sin(rotation))
        point[1] = (point_0*math.sin(rotation)) + (point_1*math.cos(rotation))
    return cube_temp

def get_cube_y_rotation(cube, rotation):
    cube_temp = copy.deepcopy(cube)
    for point in cube_temp:
        point_0 = copy.copy(point[0])
        point_2 = copy.copy(point[2])
        point[0] = (point_0*math.cos(rotation)) - (point_2*math.sin(rotation))
        point[2] = (point_0*math.sin(rotation)) + (point_2*math.cos(rotation))
    return cube_temp

def get_cube_x_rotation(cube, rotation):
    cube_temp = copy.deepcopy(cube)
    for point in cube_temp:
        point_1 = copy.copy(point[1])
        point_2 = copy.copy(point[2])
        point[1] = (point_1*math.cos(rotation)) - (point_2*math.sin(rotation))
        point[2] = (point_1*math.sin(rotation)) + (point_2*math.cos(rotation))
    return cube_temp

# render
def render():
    wcl.clear()
    wcl.hide_cursor()
    display_borders()
    wcl.locate_c(5,2, 'Thank you, Gustavo Pezzi from PIKUMA!')
    rotation = 0
    while 1:
        global cube
        cube_temp = copy.deepcopy(cube)
        cube_temp = get_cube_z_rotation(cube_temp, rotation)
        cube_temp = get_cube_y_rotation(cube_temp, rotation)
        cube_temp = get_cube_x_rotation(cube_temp, rotation)

        for point in cube_temp:
            x = int((point[0])/(point[2]-camera_pos[2])*fov_fac + camera_pos[0]) 
            y = int((point[1])/(point[2]-camera_pos[2])*fov_fac + camera_pos[1])
            if point[2] >= 0.25:
                wcl.locate_c(x, y, '·')
            else:
                wcl.locate_c(x, y, '○')
        time.sleep(0.01)
        for point in cube_temp:
            x = int((point[0])/(point[2]-camera_pos[2])*fov_fac + camera_pos[0]) 
            y = int((point[1])/(point[2]-camera_pos[2])*fov_fac + camera_pos[1])
            wcl.locate_c(x, y, ' ')

        rotation += 1/(math.pi*2*10)
        if rotation > 2*math.pi:
            rotation = 0


# display borders
def display_borders():
    for x in range(1, 159):
        wcl.locate_c(x, 0, '-')
        wcl.locate_c(x, 47, '-')

    for y in range(1, 47):
        wcl.locate_c(0, y, '|')
        wcl.locate_c(159, y, '|')

render()
