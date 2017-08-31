# 1. We need classes for each position. They have an X, a Y, and a distance to
# the solution.
# 2. If neighbors of the current position aren't in the previous_positions dict,
#     we add them to the previous positions dict.
#     2a. Previous positions dict should have entries of "X_Y" format.
# 3. For the neighbors that weren't already in previous positions, we check to sentence
#     if they're a wall or open. If open, we add them to the list of positions to test.
# 4. Then, we sort the list of positions to test by their distance value, and go back
#     to 2, starting with whatever is closest to where we want to end up.
#
from sys import exit

class Position(object):

    def __init__(self, x, y, move, tested=False):
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)
        self.move = move
        self.distance = abs(31 - self.x) + abs(39 - self.y)

    def wall_check(self):
        if self.distance == 0:
            print "Success! Number of moves is %d" % position.move
            exit()
        if str(self.coordinates) in previous_positions.keys():
            return
        else:
            previous_positions[str(self.coordinates)] = self.move

        print self.move, self.coordinates
        check = ((self.x ** 2) + (3 * self.x)
                  + (2 * self.x * self.y)
                  + self.y + (self.y ** 2) + 1362)

        check = str(bin(check))
        one_check = 0
        for c in check:
            if c == '1':
                one_check += 1

        if one_check % 2 == 1:
            to_test.append(self)


start = Position(1, 1, 0)
previous_positions = {'(1, 1)': 0}

# Try to make this a dict for now. But maybe it has to be a list, if we can't
# sort it properly.
to_test = [start]

while True:
    to_test = sorted(to_test, key=lambda position: position.distance)
    test = to_test[0]

    if test.x > 1:
        new_position = Position(test.x - 1, test.y, test.move + 1)
        new_position.wall_check()

    if test.y > 1:
        new_position = Position(test.x, test.y - 1, test.move + 1)
        new_position.wall_check()

    new_position = Position(test.x + 1, test.y, test.move + 1)
    new_position.wall_check()

    new_position = Position(test.x, test.y + 1, test.move + 1)
    new_position.wall_check()

    del to_test[0]
