import numpy as np
#------------------------------------------------------------
# MOVEMENT FUNCTIONS
#------------------------------------------------------------

# Front clockwise
# Action 0
def front_clockwise(x):  
    x[6:9, 0:3] = np.fliplr(x[6:9, 0:3].transpose())
    temp1 = np.array(x[2, 0:3])
    temp2 = np.array(x[9:12, 0])
    temp3 = np.array(x[15, 0:3])
    temp4 = np.array(x[3:6, 2])
    x[2, 0:3] = np.fliplr([temp4])[0]
    x[9:12, 0] = temp1
    x[15, 0:3] = np.fliplr([temp2])[0]
    x[3:6, 2] = temp3
    return 'front_clockwise'

# Action 1
def front_anti_clockwise(x):
    front_clockwise(x)
    front_clockwise(x)
    front_clockwise(x)
    return 'front_anti_clockwise'


# Action 2
def up_clockwise(x):
    x[0:3, 0:3] = np.fliplr(x[0:3, 0:3].transpose())
    temp1 = np.array(x[12, 0:3])
    temp2 = np.array(x[9, 0:3])
    temp3 = np.array(x[6, 0:3])
    temp4 = np.array(x[3, 0:3])
    x[12, 0:3] = temp4
    x[9, 0:3] = temp1
    x[6, 0:3] = temp2
    x[3, 0:3] = temp3
    return 'up_clockwise'


# Action 3
def up_anti_clockwise(x):
    up_clockwise(x)
    up_clockwise(x)
    up_clockwise(x)
    return 'up_anti_clockwise'


# Action 4
def down_clockwise(x):
    x[15:18, 0:3] = np.fliplr(x[15:18, 0:3].transpose())
    temp1 = np.array(x[8, 0:3])
    temp2 = np.array(x[11, 0:3])
    temp3 = np.array(x[14, 0:3])
    temp4 = np.array(x[5, 0:3])
    x[8, 0:3] = temp4
    x[11, 0:3] = temp1
    x[14, 0:3] = temp2
    x[5, 0:3] = temp3
    return 'down_clockwise'



# Action 5
def down_anti_clockwise(x):
    down_clockwise(x)
    down_clockwise(x)
    down_clockwise(x)

    return 'down_anti_clockwise'


# Action 6
def left_clockwise(x):
    x[3:6, 0:3] = np.fliplr(x[3:6, 0:3].transpose())
    temp1 = np.array(x[0:3, 0])
    temp2 = np.array(x[6:9, 0])
    temp3 = np.array(x[15:18, 0])
    temp4 = np.array(x[12:15, 2])
    x[0:3, 0] = np.fliplr([temp4])[0]
    x[6:9, 0] = temp1
    x[15:18, 0] = temp2
    x[12:15, 2] = np.fliplr([temp3])[0]

    return 'left_clockwise'


# Action 7
def left_anti_clockwise(x):
    left_clockwise(x)
    left_clockwise(x)
    left_clockwise(x)
    return 'left_anti_clockwise'


# Action 8
def right_clockwise(x):

    x[9:12, 0:3] = np.fliplr(x[9:12, 0:3].transpose())
    temp1 = np.array(x[0:3, 2])
    temp2 = np.array(x[12:15, 0])
    temp3 = np.array(x[15:18, 2])
    temp4 = np.array(x[6:9, 2])
    x[0:3, 2] = temp4
    x[12:15, 0] = np.fliplr([temp1])[0]
    x[15:18, 2] = np.fliplr([temp2])[0]
    x[6:9, 2] = temp3

    return 'right_clockwise'



# Action 9
def right_anti_clockwise(x):
    right_clockwise(x)
    right_clockwise(x)
    right_clockwise(x)
    return 'right_anti_clockwise'



# Action 10
def back_clockwise(x):

    x[12:15, :] = np.fliplr(x[12:15, :].transpose())
    temp1 = np.array(x[0, 0:3])
    temp2 = np.array(x[3:6, 0])
    temp3 = np.array(x[17, 0:3])
    temp4 = np.array(x[9:12, 2])
    x[0, 0:3] = temp4
    x[3:6, 0] = np.fliplr([temp1])[0]
    x[17, 0:3] = temp2
    x[9:12, 2] = np.fliplr([temp3])[0]
    return 'back_clockwise'



# Action 11
def back_anti_clockwise(x):
    back_clockwise(x)
    back_clockwise(x)
    back_clockwise(x)
    return 'back_anti_clockwise'


def print_cube(x):
    print("             ", x[0, 0:3])
    print("             ", x[1, 0:3])
    print("             ", x[2, 0:3])
    print(x[3, 0:3], x[6, 0:3], x[9, 0:3], x[12, 0:3])
    print(x[4, 0:3], x[7, 0:3], x[10, 0:3], x[13, 0:3])
    print(x[5, 0:3], x[8, 0:3], x[11, 0:3], x[14, 0:3])
    print("             ", x[15, 0:3])
    print("             ", x[16, 0:3])
    print("             ", x[17, 0:3])


distance_array = np.array([
    [[0, 0, 2], [1, 0, 2], [2, 0, 2]], # corner 0
    [[0, 0, 1], [1, 0, 1], [2, 0, 1]],
    [[0, 0, 0], [1, 0, 0], [2, 0, 0]], # corner 2
    [[0, 0, 2], [0, 0, 1], [0, 0, 0]], # corner 3 
    [[0, 1, 2], [0, 1, 1], [0, 1, 0]],
    [[0, 2, 2], [0, 2, 1], [0, 2, 0]], # corner 5
    [[0, 0, 0], [1, 0, 0], [2, 0, 0]], # corner 6
    [[0, 1, 0], [1, 1, 0], [2, 1, 0]],
    [[0, 2, 0], [1, 2, 0], [2, 2, 0]], # corner 8
    [[2, 0, 0], [2, 0, 1], [2, 0, 2]], # corner 9
    [[2, 1, 0], [2, 1, 1], [2, 1, 2]],
    [[2, 2, 0], [2, 2, 1], [2, 2, 2]], # corner 11
    [[2, 0, 2], [1, 0, 2], [0, 0, 2]], # corner 12
    [[2, 1, 2], [1, 1, 2], [0, 1, 2]],
    [[2, 2, 2], [1, 2, 2], [0, 2, 2]], # corner 14
    [[0, 2, 0], [1, 2, 0], [2, 2, 0]], # corner 15
    [[0, 2, 1], [1, 2, 1], [2, 2, 1]],
    [[0, 2, 2], [1, 2, 2], [2, 2, 2]], # corner 17
])


def manhattan_distance(cube, i, z, corner):
    # c de corner xd
    c1 = distance_array[i, z]
    center = None
    # Identify where's the center of the color in position (i, z)
    # It could be in list number 1, 4, 7... of the cube
    for c in [1, 4, 7, 10, 13, 16]:
        if cube[i, z] == cube[c, 1]:
            center = c
            break
    # Checks Manhattan distance to the four corner positions of the target face
    if corner:
        c2 = distance_array[center - 1, 0]
        d1 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = distance_array[center - 1, 2]
        d2 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = distance_array[center + 1, 0]
        d3 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = distance_array[center + 1, 2]
        d4 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        return min(d1, d2, d3, d4)
    else:
        c2 = distance_array[center - 1, 1]
        d1 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = distance_array[center, 0]
        d2 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = distance_array[center, 2]
        d3 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        c2 = distance_array[center + 1, 1]
        d4 = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
        return min(d1, d2, d3, d4)

def korf_heuristic(cube):
    # https://www.diva-portal.org/smash/get/diva2:816583/FULLTEXT01.pdf
    corners = 0
    edges = 0
    for i in range(18):
        # If it is the top or bottom row on a face it has edges and corners
        if i % 3 == 0 or i % 3 == 2:
            corners = corners + manhattan_distance(cube, i, 0, True) + manhattan_distance(cube, i, 2, True)
            edges_1 = edges + manhattan_distance(cube, i, 1, False)
        else:
        # If it is the middle row of a face it only has edges
            edges_2 = edges + manhattan_distance(cube, i, 0, False) + manhattan_distance(cube, i, 2, False)
    return max(corners / 8, edges_1 / 6, edges_2 /6)