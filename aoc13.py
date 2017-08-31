from sys import exit

class Position(object):

    def __init__(self, x, y, move):
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)
        self.move = move
        self.distance = abs(31 - self.x) + abs(39 - self.y)

    def wall_check(self):
        if self.distance == 0:
            print "Success! Number of moves is %d" % self.move
            exit()

        if str(self.coordinates) in previous_positions.keys():
            return
        else:
            previous_positions[str(self.coordinates)] = self.move

        check = ((self.x ** 2) + (3 * self.x) + (2 * self.x * self.y)
                  + self.y + (self.y ** 2) + 1362)

        check = str(bin(check))
        one_check = 0
        for c in check:
            if c == '1':
                one_check += 1

        if one_check % 2 == 0:
            to_test.append(self)


start = Position(1, 1, 0)
previous_positions = {'(1, 1)': 0}
to_test = [start]

while True:
    to_test = sorted(to_test, key=lambda position: position.distance)
    test = to_test[0]

    if test.x > 0:
        new_position = Position(test.x - 1, test.y, test.move + 1)
        new_position.wall_check()

    if test.y > 0:
        new_position = Position(test.x, test.y - 1, test.move + 1)
        new_position.wall_check()

    new_position = Position(test.x + 1, test.y, test.move + 1)
    new_position.wall_check()

    new_position = Position(test.x, test.y + 1, test.move + 1)
    new_position.wall_check()

    del to_test[0]
