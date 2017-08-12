from sys import exit


step_number = 0

previous_positions = []


class Map(object):
## variables: th, pl, st, pr, ru, with chip and gen variables. also: elevator
    def __init__(self, item_floor):
        self.item_floor = item_floor


    def legality_check(self):
        """This checks to see if a state is legal, and returns False if not"""
        if (self.item_floor[0] != self.item_floor[1]) and (self.item_floor[0]
            in [self.item_floor[3], self.item_floor[5], self.item_floor[7],
            self.item_floor[9]]):
            return False
        elif (self.item_floor[2] != self.item_floor[3]) and (self.item_floor[2]
            in [self.item_floor[1], self.item_floor[5], self.item_floor[7],
            self.item_floor[9]]):
            return False
        elif (self.item_floor[4] != self.item_floor[5]) and (self.item_floor[5]
            in [self.item_floor[3], self.item_floor[1], self.item_floor[7],
            self.item_floor[9]]):
            return False
        elif (self.item_floor[6] != self.item_floor[7]) and (self.item_floor[6]
            in [self.item_floor[3], self.item_floor[5], self.item_floor[1],
            self.item_floor[9]]):
            return False
        elif (self.item_floor[8] != self.item_floor[9]) and (self.item_floor[8]
            in [self.item_floor[3], self.item_floor[5], self.item_floor[7],
            self.item_floor[1]]):
            return False
        else:
            return True


# entries in the list that goes into a class correspond to the variables as
# listed in object_names (below)
starting_positions = [1, 1, 2, 1, 2, 1, 3, 3, 3, 3, 1]

object_names = ['th_chip', 'th_gen', 'pl_chip', 'pl_gen', 'st_chip',
                'st_gen', 'pr_chip', 'pr_gen', 'ru_chip', 'ru_gen']

current_move_positions = [Map(starting_positions)]



while step_number < 9:

    print step_number
    legal_next_steps = []

    for position in current_move_positions:
        success = True
        # check to see if any given position is a winner.
        for item in position.item_floor:
            if item != 4:
                success = False
                break
        if success == True:
            print step_number
            exit()


        # movable object list is what single or double item combos are on the
        # same floor as the elevator
        movable_object_list = []
        # temporary storage of movable two-item combos, so we don't amend
        # movable_object_list while we're reading from it.
        duo_object_temp = []


        for x in xrange(0, 10):
            if position.item_floor[x] == position.item_floor[10]:
                movable_object_list.append(object_names[x])

        for x in xrange(0, len(movable_object_list)):
            for y in xrange(x + 1, len(movable_object_list)):
                duo = movable_object_list[x] + " " + movable_object_list[y]
                duo_object_temp.append(duo)

        for item in duo_object_temp:
            movable_object_list.append(item)


        # check to see what legal moves by going up the elevator exist.
        # if elevator == 4, then we're at the top floor, so no need to check.
        if position.item_floor[10] < 4:
            for item in movable_object_list:

                new_layout = []
                for i in position.item_floor:
                    new_layout.append(i)

                for x in xrange(0, len(object_names)):
                    if object_names[x] in item:
                        new_layout[x] += 1

                new_layout[10] += 1
                test = Map(new_layout)
                legal = test.legality_check()

                if legal == False:
                    pass
                elif new_layout not in previous_positions:
                    legal_next_steps.append(test)

        # possible moves going down. If elevator == 1, we're at bottom floor,
        # so no need to check.
        if position.item_floor[10] > 1:
            for item in movable_object_list:

                new_layout = []
                for i in position.item_floor:
                    new_layout.append(i)

                for x in xrange(0, len(object_names)):
                    if object_names[x] in item:
                        new_layout[x] -= 1

                new_layout[10] -= 1
                test = Map(new_layout)
                legal = test.legality_check()
                if legal == False:
                    pass
                elif new_layout not in previous_positions:
                    legal_next_steps.append(test)


        previous_positions.append(position.item_floor)
    current_move_positions = legal_next_steps
    step_number += 1



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
