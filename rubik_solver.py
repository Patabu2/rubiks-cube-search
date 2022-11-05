import numpy as np
import rubik_functions as rf
import time

moves_list = [
    rf.front_clockwise,
    rf.front_anti_clockwise,
    rf.up_clockwise,
    rf.up_anti_clockwise,
    rf.down_clockwise,
    rf.down_anti_clockwise,
    rf.left_clockwise,
    rf.left_anti_clockwise,
    rf.right_clockwise,
    rf.right_anti_clockwise,
    rf.back_clockwise,
    rf.back_anti_clockwise
]


class StateNode():
    def __init__(self, cube, g, h, parent, move, s):
        self.cube = cube
        self.g = g # Path cost from initial state to state n
        self.h = h # Estimated cost of shortest path from state n to goal
        self.parent = parent
        self.move = move
        self.s = s # A string of all the letters in the cube

    def is_goal(self):
        if self.h != 0:
            return False
        else:
            return True

    def act(self, i):
        return moves_list[i](self.cube)

    def cube_to_string(self):
        letter_list = []
        for i in range(18):
            for j in range(3):
                letter_list.append(self.cube[i, j])
        self.s = "".join(letter_list)
        return self.s

    def is_cube_in_ascendants(self, pariente):
        ascendant = pariente.parent

        while ascendant is not None:
            if np.array_equal(ascendant.cube, self.cube):
                return True
            ascendant = ascendant.parent
        return False

    def is_cube_in_frontier(self, frontier):
        for node in frontier:
            if np.array_equal(node.cube, self.cube):
                return True
        return False

#----------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A STAR ALGORITHM
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#----------------------------------------------------
def expand(state_node, heuristic_function):
    '''
    Take a parent cube and apply all 12 possible movements to it to generate children

    @state_node: object of type StateNode containing the information of the cube
    '''
    child_list = []
    for i in range(12):
        child_node = StateNode(
            cube = state_node.cube.copy(),
            g = state_node.g + 1,
            h = None,
            s = None,
            parent = state_node,
            move = None
        )

        child_node.move = child_node.act(i)
        child_node.s = child_node.cube_to_string()
        child_node.h = heuristic_function(child_node.cube)

        child_list.append(child_node)
    return child_list


def a_star(root, heuristic_function):
    '''
    Take some object representing a problem and solve it.
    The problem it solves depends on the class that its passed as root, as well as how the expand function is defined.
    Also. The specific way to calculate h and g cary from problem to problem.

    
    @root: object of class StateNode.
    @
    '''
    root.h =  heuristic_function(root.cube)
    frontier = [root]
    reached = {root.s: root}
    nodes = 1

    # While there are elements in the frontier, keep digging
    while frontier:
        # Select the first element in the frontier
        current_node = frontier.pop(0)

        # If that element is a goal_state. You've made it! :Dzx
        if current_node.is_goal():
            print('CUBE SOLVED!')
            print('Goal Height:', current_node.g)
            print('Final Frontier size: ', len(frontier))
            print('Nodes Generated:', nodes)
            print('Nodes explored: ', len(reached))
            rf.print_cube(current_node.cube)
            return current_node
        # If not, explore all of its children
        children = expand(current_node, heuristic_function)
        nodes += 12
        for child in children:
            if (child.s not in reached) or (child.g + child.h < reached[child.s].h + reached[child.s].g ):
                reached[child.s] = child
                frontier.append(child)
    return "Mission failed, we'll get 'em next time"




#----------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# RUN IT
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#----------------------------------------------------
# Nice initial cube of shape (18, 3)
initial_cube = np.array([
    ['Y', 'Y', 'Y'], # 0
    ['Y', 'Y', 'Y'], # 1        TOP
    ['Y', 'Y', 'Y'], # 2

    ['O', 'O', 'O'], # 3
    ['O', 'O', 'O'], # 4        LEFT
    ['O', 'O', 'O'], # 5

    ['B', 'B', 'B'], # 6
    ['B', 'B', 'B'], # 7        FRONT
    ['B', 'B', 'B'], # 8

    ['R', 'R', 'R'], # 9
    ['R', 'R', 'R'], # 10      RIGHT
    ['R', 'R', 'R'], # 11

    ['G', 'G', 'G'], # 12
    ['G', 'G', 'G'], # 13    BACK
    ['G', 'G', 'G'], # 14

    ['W', 'W', 'W'], # 15
    ['W', 'W', 'W'], # 16       BOTTOM
    ['W', 'W', 'W']  # 17
])

# Create a root node from the initial cube
root = StateNode(
    cube = initial_cube.copy(),
    g = 0,
    h = 0,
    parent = None,
    move = None,
    s = None
)

# Scramble the cube
for i in range(4):
    root.act(np.random.randint(0,12))
# Convert it to string and store it for the lookup dictionary
root.cube_to_string()


#----------------------------------------
# Print initial cube and scrambled cube
#----------------------------------------
#print('Initial cube')
#rf.print_cube(initial_cube)
#print('\n')
print('Scrambled cube')
rf.print_cube(root.cube)
print('\n')


#---------------------------------------
# Let the algorithm do its magic
#---------------------------------------'
initial_time = time.time()
node = a_star(root, rf.korf_heuristic) # The final node
end_time = time.time()

print(f'Time to solve: {round(end_time - initial_time, 2)}s\n')


# Print the whole solution path
solution_path = [node]
while node:
    node = node.parent
    if node is not None:
        solution_path.append(node)

print('FULL SOLUTION PATH')
print('\n')
for step in reversed(solution_path):
    #rf.print_cube(step.cube)
    print(step.move)

