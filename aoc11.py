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

    def __init__(self, h_chip, h_gen, l_chip, l_gen, elevator):
        self.h_chip = h_chip
        self.h_gen = h_gen
        self.l_chip = l_chip
        self.l_gen = l_gen
        self.item_list = [self.h_chip, self.h_gen, self.l_chip, self.l_gen]
        self.elevator = elevator



    def legality_check(self):
        """This checks to see if a state is legal, and returns False if not"""
        if (self.h_chip != self.h_gen) and (self.h_chip == self.l_gen):
            return False
        elif (self.l_chip != self.l_gen) and (self.l_chip == self.h_gen):
            return False
        else:
            return True





current_move_positions = [Map(1, 2, 1, 3, 1)]

while step_number < 15:
    # all this is creating objects of potential future positions
    print step_number
    legal_next_steps = []
    for position in current_move_positions:

        if (position.h_chip == 4 and position.h_gen == 4 and
        position.l_chip == 4 and position.l_gen == 4):
            print step_number
            exit()


        this_map_layout = [
            position.h_chip,
            position.h_gen,
            position.l_chip,
            position.l_gen
        ]
        object_names = ['h_chip', 'h_gen', 'l_chip', 'l_gen']

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

        for item in movable_object_list:
            if position.elevator == 4:
                pass
            else:
                new_layout = [position.h_chip, position.h_gen,
                              position.l_chip, position.l_gen]

                for x in xrange(0, len(object_names)):
                    if object_names[x] in item:
                        new_layout[x] += 1

                test = Map(new_layout[0], new_layout[1],
                    new_layout[2], new_layout[3], position.elevator + 1)
                legal = test.legality_check()
                if test not in previous_positions and legal == True:
                    legal_next_steps.append(test)

        for item in movable_object_list:
            if position.elevator == 1:
                pass
            else:
                new_layout = [position.h_chip, position.h_gen,
                              position.l_chip, position.l_gen]

                for x in xrange(0, len(object_names)):
                    if object_names[x] in item:
                        new_layout[x] -= 1

                test = Map(new_layout[0], new_layout[1],
                    new_layout[2], new_layout[3], position.elevator - 1)
                legal = test.legality_check()
                if test not in previous_positions and legal == True:
                    legal_next_steps.append(test)



    previous_positions.append(position)

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
