import re
from sys import exit

class Node(object):

    def __init__(self, x, y, traveled):
        self.x = x
        self.y = y
        self.traveled = traveled
        self.to_go = (30 - self.x) + self.y
        self.coordinates = (self.x, self.y)
        self.data_coordinates = (30, 0)


def find_legal_positions(test):

    prev_position_tuple = (test.x, test.y, test.data_coordinates)
    if prev_position_tuple in previous_positions:
        return
    else:
        previous_positions[prev_position_tuple] = test.traveled


    if (test.x - 1, test.y) in legal_nodes:
        new_position = Node(test.x - 1, test.y, test.traveled + 1)
        if test.data_coordinates == new_position.coordinates:
            new_position.data_coordinates = (test.x, test.y)
        else:
            new_position.data_coordinates = test.data_coordinates
        legal_positions.append(new_position)

    if (test.x + 1, test.y) in legal_nodes:
        new_position = Node(test.x + 1, test.y, test.traveled + 1)
        if test.data_coordinates == new_position.coordinates:
            new_position.data_coordinates = (test.x, test.y)
        else:
            new_position.data_coordinates = test.data_coordinates
        legal_positions.append(new_position)

    if (test.x, test.y - 1) in legal_nodes:
        new_position = Node(test.x, test.y - 1, test.traveled + 1)
        if test.data_coordinates == (test.x, test.y - 1):
            new_position.data_coordinates = test.coordinates
        else:
            new_position.data_coordinates = test.data_coordinates
        legal_positions.append(new_position)

    if (test.x, test.y + 1) in legal_nodes:
        new_position = Node(test.x, test.y + 1, test.traveled + 1)
        if test.data_coordinates == new_position.coordinates:
            new_position.data_coordinates = test.coordinates
        else:
            new_position.data_coordinates = test.data_coordinates
        legal_positions.append(new_position)


node_template = ".*?-x(\d*)\-y(\d*) \s*(\d*)T \s*(\d*)T \s*(\d*)T"
legal_nodes = {}
previous_positions = {}
empty_node = None
data = (30, 0)
max_storage = 92 # 92 == the availability of the starting empty node. Based
                 # on prior testing, all nodes can be swapped with one another
                 # except those with a starting usage > 92. So we can safely
                 # say that things larger than 92 are walls, and everything
                 # else is an open space.

# This gets us our starting position, and a list of positions we can swap into
with open("aoc22.txt") as f:
    for line in f:
        stats = re.match(node_template, line, re.I)
        if stats:
            x_coord = int(stats.group(1))
            y_coord = int(stats.group(2))
            used = int(stats.group(4))
            available = int(stats.group(5))
            coord = (x_coord, y_coord)
            size = int(stats.group(3))
            if used == 0:
                start_position = Node(x_coord, y_coord, 0)
                print start_position.x, start_position.y
            if used < max_storage:
                legal_nodes[coord] = "open"

legal_positions = [start_position]

while True:

    find_legal_positions(legal_positions[0])

    if legal_positions[0].to_go == 0:
        previous_positions = {}
        break

    del legal_positions[0]
    legal_positions = sorted(legal_positions,
                             key=lambda node: (node.to_go + node.traveled))

previous_positions = {}

while True:
    if legal_positions[0].data_coordinates == (0, 0):
        break
    find_legal_positions(legal_positions[0])

    del legal_positions[0]
    legal_positions = sorted(legal_positions, key=lambda node:
        node.data_coordinates[0] + node.data_coordinates[1])


print legal_positions[0].traveled
