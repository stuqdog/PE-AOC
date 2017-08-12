#
# 1. Layout map. Set floor to elevator.
#
# 1. We can just make a single class for map, and have variables set to 1, 2, 3
#    or 4 to indicate the floor. Then we put the value for items in
#    self.object_list.
# 2. Then (so long as self.steps_taken is < minimum_steps - 1), for object in
#    self.object_list: if the value is equal to floor, then add it to
#    potentially_movable_objects.
# 3. Then, for every combination of one or two items in
#    potentially_movable_objects see if moving that object (pair) up or down a
#    floor is still legal. If it is, create that state as test_class. if test
#    class doesn't appear in self.states_already_tested, then create_copy is
#    equal to test_class and put create_copy into a list of things to test.
# 3. After we finish finding out all possible states that can be legal check the
#    next states, one at a time. First step of checking a next state is to add
#    the previous state to a self.states_already_tested (probably a list). Second
#    step is to iterate up the self.steps_taken variable.
# 4. Once a map reaches final_state, then we retreat back, and set minimum_steps
#    equal to self.steps_taken.
# 5. If at any point self.steps_taken is great then minimum_steps, then we kill
#    the current path and end the loop.
#       NO THIS IS WRONG! The better way to do it is to map out every step at
#       the same time (as in, check all move 1s, then all move 2s, etc.). We
#       can track them as a "self.possible_next_steps" variable. We can track
#       already_seen_states as a global variable, because if it's being reached
#       for a second time anywhere, then we know there was a more efficient
#       (or at least equally efficient) way to get there.

from sys import exit

starting_map_features = {
    'h_chip': 1,
    'h_gen': 2,
    'l_chip': 1,
    'l_gen': 3,
    'elevator': 1,
    'steps_taken': 0,
    'previous_states': [],
    'movable_object_list': []
}
step_number = 0

legal_next_steps = []
previous_positions = []


class Map(object):
## variables: th, pl, st, pr, ru
    def __init__(self, th_chip, th_gen, pl_chip, pl_gen, st_chip,
                 st_gen, pr_chip, pr_gen, ru_chip, ru_gen, elevator):
        self.th_chip = th_chip
        self.th_gen = th_gen
        self.pl_chip = pl_chip
        self.pl_gen = pl_gen
        self.st_chip = st_chip
        self.st_gen = st_gen
        self.pr_chip = pr_chip
        self.pr_gen = pr_gen
        self.ru_chip = ru_chip
        self.ru_gen = ru_gen
        self.item_list = [self.th_chip, self.th_gen, self.pl_chip, self.pl_gen,
                          self.st_chip, self.st_gen, self.pr_chip, self.pr_gen,
                          self.ru_chip, self.ru_gen]
        self.elevator = elevator



    def legality_check(self):
        """This checks to see if a state is legal, and returns False if not"""
        if (self.th_chip != self.th_gen) and (self.th_chip in [
              self.pl_gen, self.st_gen, self.pr_gen, self.ru_gen]):
            return False
        elif (self.pl_chip != self.pl_gen) and (self.pl_chip in [
              self.th_gen, self.st_gen, self.pr_gen, self.ru_gen]):
            return False
        elif (self.st_chip != self.st_gen) and (self.st_chip in [
              self.th_gen, self.pl_gen, self.pr_gen, self.ru_gen]):
            return False
        elif (self.pr_chip != self.pr_gen) and (self.pr_chip in [
              self.th_gen, self.st_gen, self.pl_gen, self.ru_gen]):
            return False
        elif (self.ru_chip != self.ru_gen) and (self.ru_chip in [
              self.th_gen, self.st_gen, self.pr_gen, self.pl_gen]):
            return False
        else:
            return True





current_move_positions = [Map(1, 1, 2, 1, 2, 1, 3, 3, 3, 3, 1)]


while True:
    # all this is creating objects of potential future positions
    print step_number
    legal_next_steps = []

    for position in current_move_positions:
        success = True
        for item in position.item_list:
            if item != 4:
                success = False
                break
        if success == True:
            print step_number
            exit()


        this_map_layout = [
            position.th_chip,
            position.th_gen,
            position.pl_chip,
            position.pl_gen,
            position.st_chip,
            position.st_gen,
            position.pr_chip,
            position.pr_gen,
            position.ru_chip,
            position.ru_gen
        ]
        object_names = ['th_chip', 'th_gen', 'pl_chip', 'pl_gen', 'st_chip',
                        'st_gen', 'pr_chip', 'pr_gen', 'ru_chip', 'ru_gen']

        movable_object_list = []
        duo_object_temp = []


        for x in range(0, len(this_map_layout)):
            if this_map_layout[x] == position.elevator:
                movable_object_list.append(object_names[x])

        for x in range(0, len(movable_object_list)):
            for y in range(x + 1, len(movable_object_list)):
                duo = movable_object_list[x] + " " + movable_object_list[y]
                duo_object_temp.append(duo)

        # after this, we have a list of items that can possibly be moved
        for item in duo_object_temp:
            movable_object_list.append(item)


        if position.elevator == 4:
            pass
        else:
            for item in movable_object_list:

                new_layout = [position.th_chip, position.th_gen,
                    position.pl_chip, position.pl_gen, position.st_chip,
                    position.st_gen, position.pr_chip, position.pr_gen,
                    position.ru_chip, position.ru_gen]

                for x in xrange(0, len(object_names)):
                    if object_names[x] in item:
                        new_layout[x] += 1

                test = Map(new_layout[0], new_layout[1], new_layout[2],
                    new_layout[3], new_layout[4], new_layout[5], new_layout[6],
                    new_layout[7], new_layout[8], new_layout[9],
                    position.elevator + 1)
                legal = test.legality_check()
                repeat_test = ''
                for item in test.item_list:
                    repeat_test += str(item)
                if repeat_test in previous_positions:
                    legal = False
                # if test not in previous_positions and legal == True:
                if legal == True:
                    legal_next_steps.append(test)

        if position.elevator == 1:
            pass
        else:
            for item in movable_object_list:
                new_layout = [position.th_chip, position.th_gen,
                    position.pl_chip, position.pl_gen, position.st_chip,
                    position.st_gen, position.pr_chip, position.pr_gen,
                    position.ru_chip, position.ru_gen]

                for x in xrange(0, len(object_names)):
                    if object_names[x] in item:
                        new_layout[x] -= 1

                test = Map(new_layout[0], new_layout[1], new_layout[2],
                    new_layout[3], new_layout[4], new_layout[5], new_layout[6],
                    new_layout[7], new_layout[8], new_layout[9],
                    position.elevator - 1)
                legal = test.legality_check()
                repeat_test = ''
                for item in test.item_list:
                    repeat_test += str(item)
                if repeat_test in previous_positions:
                    legal = False
                if legal == True:
                # if legal == True:
                    legal_next_steps.append(test)


        prev_position = ''
        for item in position.item_list:
            prev_position += str(item)
        previous_positions.append(prev_position)
    current_move_positions = legal_next_steps
    step_number += 1





        # if position.h_chip == position.elevator:
        #     movable_object_list.append('h_chip')
        # if position.h_gen == position.elevator:
        #     movable_object_list.append('h_gen')
        # if position.l_chip == position.elevator:
        #     movable_object_list.append('l_chip')
        # if position.l_gen == position.elevator:
        #     movable_object_list.append('l_gen')
