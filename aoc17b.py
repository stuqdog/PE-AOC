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
            solution = self.path_taken
            # Need to return here to prevent from continuing on from (4, 4)
            return solution

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

        return None


starting_position = Position(1, 1, '')
current_positions = [starting_position]
solution = ''
step = 0

while True:

    legal_next_steps = []

    for position in current_positions:
        solution_check = position.test_new_direction()
        if solution_check != None:
            solution = solution_check

    if legal_next_steps == []:
        print "Final step reached! It is %s: length is %d" % (
            solution, len(solution))
        exit()
    current_positions = legal_next_steps
    step += 1
    # print step
