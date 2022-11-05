# Solving a Rubik's cube with the A* algorithm.

The A* search (A-star search) algorithm belongs to a family of algorithms called Informed Search Strategies, that use heuristics to determine the closeness of the current state to a desired goal state. More specifically, A* is a best-first search algorithm that uses the evaluation function $f(n) = g(n) + h(n)$, where $g(n)$ is the path cost from the initial state to the current node $n$, and $h(n)$ is the estimated goal of the shortest path from the current node $n$ to a goal state. Therefore, $f(n)$ is the estimated cost of the best path that continues from $n$ to a goal. At each step, A* expands the node in the frontier that has the best $f(n)$ (usually the smallest value).

In this implementation of the Rubik's Cube solver, Korf's heuristic function is used as described by Harpeet Kaur (https://www.diva-portal.org/smash/get/diva2:816583/FULLTEXT01.pdf). Korf's heuristic uses the Manhattan distance to approximate the number of spaces that a square  has to move to be in the final position. Therefore, a simple way to view Korf's heuristic is that we are calculating the total number of steps that we need to take to put all the squares in their final place by their distance to the center square that has the same color as them.

The cube is represented as a NumPy array of dimensions $18\times3$ in the file `rubik_solver.py`. The A* algorithm implementation is also in `rubik_solver.py`. There are 12 possible actions for the cube, and all of them are defined in the file `rubik_functions.py`. Korf's heuristic is also defined in `rubik_functions.py`.

One limitation of this implementation is the fact that the possible paths increase exponentially by a factor of 12 (the number of possible actions) at each level in the search tree. Therefore, if the cube is in an initial state that is hard to solve, the algorithm will take a long time to solve it.

A solution to this is the IDA* algorithm, which truncates the depth of the search at a pre-defined level if the goal state is not reached and continues through another path. However, this implementation is left as future work.

To run the code, simply make sure that NumPy is installed with the command `pip install NumPy`, and afterwards run `rubik_solver.py`.
