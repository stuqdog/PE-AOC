# A* TIME YEAHHHH
#
# So aoc22 gives us a list of all nodes. But it's not good enough, now we need nodes
# to have an x and y coordinate instead of a name. So first we do that. then we use
# A* to move the single empty node over to (0, 30), then use A* to move the data in (0, 30)
# over to (0, 0)
#
#
# create a dict of nodes, key = (x, y) tuple. value = class(x, y, used, available,
#  , distance_traveled, distance_gone target_data=False)
#
#
#
# so: create a class. make an instance of it for each node. If it's the zero node,
# then that's our start_position.
#
# then, current_positions = [start_position]
# for position[0]: find new legal positions, add them to current_positions. iterate up steps taken
#
# then, order current_positions[] based on (steps_taken + distance_to_target), and do it again
# at all times, the goal should be moving the empty thing over. so empty space node is special somehow
# do this until the empty position is next to (30, 0)
#
# then, do it again, but moving the data at (30, 0) over to (0, 0).

#PRoblem: when we test a new move, we empty out one node next and fill another
# but then if we want to go back and test other moves, that node is emptied again.
# So gotta find a way to keep whether a node is empty stable without having to
# copy all 961 nodes for all possible moves.

# what we _could_ do is just have the node we're moving (the empty one) be able to move
# so long as its capacity is greater than wherever it's moving to's used.
# then, set its capacity to whatever the capacity is of where it's moving. That should work.
# when moving the data to the start point, our heuristic isn't going to be how close
# the empty is (even though we're moving the empty,) but how close the target is.

# HOW ABOUT THIS. Just find out which nodes can't swap with the the empty one because
# they have too much data. Then we just say those are walls, and everything else is
# open. Then, when we reach the data, we change our heuristic to how close the data
# is, rather than how close the empty square is.


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


# class Target(Node):
#
#     def __init__(self, x, y, used, avail, special=True):
#         super(Target, self).__init__(x, y, used, avail)



def find_legal_positions(test):

    prev_position_tuple = (test.x, test.y, test.data_coordinates)
    if prev_position_tuple in previous_positions:
        return
    else:
        previous_positions[prev_position_tuple] = test.traveled

    if (test.x - 1, test.y) in legal_nodes:
        new_position = Node(test.x - 1, test.y, test.traveled + 1)
        if test.data_coordinates == new_position.coordinates:
            new_position.data_coordinates = test.coordinates
        legal_positions.append(new_position)

    if (test.x + 1, test.y) in legal_nodes:
        new_position = Node(test.x + 1, test.y, test.traveled + 1)
        if test.data_coordinates == new_position.coordinates:
            new_position.data_coordinates = test.coordinates
        legal_positions.append(new_position)

    if (test.x, test.y - 1) in legal_nodes:
        new_position = Node(test.x, test.y - 1, test.traveled + 1)
        if test.data_coordinates == (test.x, test.y - 1):
            new_position.data_coordinates = (test.x, test.y)
        legal_positions.append(new_position)

    if (test.x, test.y + 1) in legal_nodes:
        new_position = Node(test.x, test.y + 1, test.traveled + 1)
        if test.data_coordinates == new_position.coordinates:
            new_position.data_coordinates = test.coordinates
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
            elif used < max_storage:
                legal_nodes[coord] = "open"

legal_positions = [start_position]

while True:

    find_legal_positions(legal_positions[0])
    #print legal_positions[0].to_go
    #if legal_positions[0].to_go == 1:
    if legal_positions[0].coordinates == (29, 0):
        print "WE ARE HERE"
        #print len(legal_positions)
        break

    del legal_positions[0]
    legal_positions = sorted(legal_positions, key=lambda node: node.to_go)

while True:
    if legal_positions[0].data_coordinates == (0, 0):
        break
    find_legal_positions(legal_positions[0])

    del legal_positions[0]
    legal_positions = sorted(legal_positions, key=lambda node:
                        node.data_coordinates[0] + node.data_coordinates[1])


print legal_positions[0].traveled
#
# print "THIS IS OKAY"
# print lowest_size
# print highest_used


        #
        # if used != 0:
        #     base_node_layout[coord] = Node(x_coord, y_coord, used, avail)
        # else:
        #     base_node_layout[coord] = Empty(x_coord, y_coord, used, avail,
        #                               0, abs(30 - x_coord) + abs(0 - y_coord))
