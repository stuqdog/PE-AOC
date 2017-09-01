# 1. Create a class for positions.
#   Class elements: x, y, path_taken. Add path_taken to base code and
#   then hash it, determine if u/d/l/r can be visited. if they can, hash create new
#   class that moves in that direction, add it to legal_next_steps.
# 2. After you've done that for all positions, current_positions = legal_next_steps
# 3. rinse, repeat.
import md5
from sys import exit

class Position(object):

    def __init__(self, x, y, path_taken):
        self.x = x
        self.y = y
        self.path_taken = path_taken
        self.hash = "pgflpeqp" + path_taken

    def test_new_direction(self):

        if self.x == 4 and self.y == 4:
            print "Success! Path is: %s" % self.path_taken
            exit()

        hash_test = md5.new(self.hash).hexdigest()

        if hash_test[0] in ['b', 'c', 'd', 'e', 'f'] and self.y > 1:
            new_position = Position(self.x, self.y - 1, self.path_taken + 'U')
            legal_next_steps.append(new_position)
        if hash_test[1] in ['b', 'c', 'd', 'e', 'f'] and self.y < 4:
            new_position = Position(self.x, self.y + 1, self.path_taken + 'D')
            legal_next_steps.append(new_position)
        if hash_test[2] in ['b', 'c', 'd', 'e', 'f'] and self.x > 1:
            new_position = Position(self.x - 1, self.y, self.path_taken + 'L')
            legal_next_steps.append(new_position)
        if hash_test[3] in ['b', 'c', 'd', 'e', 'f'] and self.x < 4:
            new_position = Position(self.x + 1, self.y, self.path_taken + 'R')
            legal_next_steps.append(new_position)



starting_position = Position(1, 1, '')
current_positions = [starting_position]

while True:

    legal_next_steps = []

    for position in current_positions:
        position.test_new_direction()

    if legal_next_steps == []:
        print "No legal moves remain. This is an error."
        exit()
    current_positions = legal_next_steps
