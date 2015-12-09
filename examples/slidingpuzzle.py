#!/usr/bin/python

import os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  + '/' + 'solvertrainer'

import sys
sys.path.insert(0, project_path)

import solver

TOP = 0
BOTTOM = 1
LEFT = 2
RIGHT = 3
direction_map = ["top", "bottom", "left", "right"]

class SlidingPuzzleStateManager:

    def __init__(self):
        self.matrix = range(16) # 15 is the "blank" tile

    def change_state(self, matrix):
        self.matrix = matrix

    def get_allowed_directions(self):
        i = self.matrix.index(15)
        directions = []
        if(i > 3): directions.append(TOP)
        if(i < 12): directions.append(BOTTOM)
        if(i%4 != 0): directions.append(LEFT)
        if(i%4 != 3): directions.append(RIGHT)
        return directions

    def get_allowed_operations(self):
        # there is only one allowed operation: "move"
        # it takes one argument, which has 4 possible options: top, bottom, left or right
        # this is mapped to an integer range 0 to 4
        # return [
        #     {
        #         "name" : "move",
        #         "arguments" : [
        #             { "type" : "list", "items" : self.get_allowed_directions() }
        #         ]
        #     }
        # ]
        directions = self.get_allowed_directions()
        operations = []
        for direction in directions:
            operations.append({ "name" : direction_map[direction] })
        return operations

    # move the blank tile to top/bottom/left/right
    # check if direction is allowed, ie if tile is on the edge
    # if not, swap the blank tile at self.blank with the other tile
    def move(self, direction):
        i = self.matrix.index(15)
        directions = self.get_allowed_directions()
        if(not direction in directions):
            return False
        new_i = [i-4, i+4, i-1, i+1][direction]
        self.matrix[i], self.matrix[new_i] = self.matrix[new_i], self.matrix[i]
        return True

    def top(self):
        return self.move(TOP)

    def bottom(self):
        return self.move(BOTTOM)

    def left(self):
        return self.move(LEFT)

    def right(self):
        return self.move(RIGHT)


    # this is the key part:
    # on solution, when all tiles are its position, return 0
    # more the tiles are far from its position, add distance
    # also add distance of blank tile from each misplaced tile
    def get_distance(self):
        distance = 0
        blank = self.matrix.index(15)
        for i in self.matrix:
            x1, y1 = i/4, i%4
            x2, y2 = self.matrix[i]/4, self.matrix[i]%4
            x3, y3 = blank/4, blank%4 # blank tile
            tile_distance = abs(x1-x2) + abs(y1-y2)
            if(tile_distance > 0):
                tile_distance += abs(x1-x3) + abs(y1-y3)
            distance += tile_distance
        return distance

    def get_state_code(self):
        # convert the state to 4-byte integer
        code = 0
        for i in range(15):
            code |= self.matrix[i]
        return code


    #DEBUG method
    def print_state(self):
        print(self.matrix)
        print("distance: " + str(self.get_distance()))


def solve_matrix(matrix):
    state_manager = SlidingPuzzleStateManager()
    state_manager.change_state(matrix)
    # state_manager.print_state()
    solution = solver.solve(state_manager)
    simple_path = []
    for operation in solution["path"]:
        simple_path.append(operation["operation"])
        # direction = operation["arguments"][0]
        # simple_path.append(direction_map[direction])
    if(solution["distance"] == 0):
        status = "success"
    else:
        status = "failure"
    return { "status" : status, "path": simple_path }

# DEBUG code to run from command line
if __name__ == "__main__":
    matrix = range(16)
    matrix[14], matrix[15] = matrix[15], matrix[14]
    solution = solve_matrix(matrix)
    print(solution)

