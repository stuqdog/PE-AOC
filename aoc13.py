class Position(object):

    part_one = 0
    part_two = 0

    def __init__(self, x, y, move):
        self.x = x
        self.y = y
        self.coordinates = (x, y)
        self.move = move
        self.distance = abs(31 - self.x) + abs(39 - self.y)
        self.heuristic = self.move + self.distance

    def wall_check(self):
        if self.distance == 0:
            Position.part_one = self.move

        if str(self.coordinates) in previous_positions:
            return
        else:
            previous_positions[str(self.coordinates)] = self.move

        check = ((self.x ** 2) + (3 * self.x) + (2 * self.x * self.y)
                  + self.y + (self.y ** 2) + 1350)

        binary_check = str(bin(check))
        one_check = sum(1 for i in binary_check if i == '1')

        if one_check % 2 == 0:
            to_test.append(self)



start = Position(1, 1, 0)
previous_positions = {'(1, 1)': 0}
to_test = [start]
steps = 0

while not Position.part_one:
    if to_test[0].move <= 50:
        to_test = sorted(to_test, key=lambda position: position.move)
    else:
        to_test = sorted(to_test, key=lambda position: position.heuristic)
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

    if test.move <= 50:
        Position.part_two += 1
    del to_test[0]

print(Position.part_one)
print(Position.part_two)
