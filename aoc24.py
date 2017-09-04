import string

class Position(object):

    def __init__(self, x, y, visited, steps):
        self.x = x
        self.y = y
        self.visited = visited
        self.steps = steps
        self.heuristic = steps

    def update_heuristic(self):
        update = 0
        for x in range(0, 8):
            update += ((abs(spot_coordinates[str(x)][0] - self.x)
                + abs(spot_coordinates[str(x)][1] - self.y)) * self.visited[x])
        self.heuristic = update + self.steps



def find_legal_positions(x, y, visited, steps):

    if str((x, y, visited)) in previous_positions:
        return

    previous_positions[str((x, y, visited))] = steps

    if layout[y + 1][x] != "#":
        new_visited = visited[:]
        new_position = Position(x, y + 1, new_visited, steps + 1)
        new_position.update_heuristic()
        to_check.append(new_position)

    if layout[y - 1][x] != '#':
        new_visited = visited[:]
        new_position = Position(x, y - 1, new_visited, steps + 1)
        new_position.update_heuristic()
        to_check.append(new_position)

    if layout[y][x + 1] != '#':
        new_visited = visited[:]
        new_position = Position(x + 1, y, new_visited, steps + 1)
        new_position.update_heuristic()
        to_check.append(new_position)

    if layout[y][x - 1] != '#':
        new_visited = visited[:]
        new_position = Position(x - 1, y, new_visited, steps + 1)
        new_position.update_heuristic()
        to_check.append(new_position)


count_x, count_y = 0, 0
previous_positions = {}
spots = []
# spot_coordinates assigns tuples of (x-val, y-val) to the must_visit spots
spot_coordinates = {}
layout = []
check_counter = 8
solution = 0

with open("aoc24.txt") as f:
    for line in f:
        new_line = []
        for c in line:
            new_line.append(c)
            if c in string.digits:
                spots.append(1)
                spot_coordinates[c] = (count_x, count_y)
            if c == "0":
                start_x, start_y = count_x, count_y
            count_x += 1
        layout.append(new_line)
        count_y += 1
        count_x = 0

print spots
start_position = Position(start_x, start_y, spots, 0)
to_check = [start_position]

check_counter = 8


while len(to_check) != 0:

    current_tile = layout[to_check[0].y][to_check[0].x]
    if current_tile in string.digits:
        to_check[0].visited[int(current_tile)] = 0

    visited_check = sum(to_check[0].visited[x] for x in range(0, 8))
    if visited_check == 0:
        if solution == 0:
            solution = to_check[0].steps
        else:
            if to_check[0].steps < solution:
                solution = to_check[0].steps

    if visited_check < check_counter:
        print check_counter
        check_counter = visited_check

    find_legal_positions(to_check[0].x, to_check[0].y, to_check[0].visited,
                         to_check[0].steps)

    del to_check[0]
    to_check = sorted(to_check, key=lambda position: position.heuristic)

    if solution != 0:
        while len(to_check) != 0 and to_check[0].steps > solution:
            del to_check[0]

print solution
