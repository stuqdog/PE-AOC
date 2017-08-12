from sys import exit


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
                repeat_test = ''
                for item in test.item_list:
                    repeat_test += str(item)
                repeat_test += str(test.elevator)
                if repeat_test in previous_positions:
                    legal = False
                if legal == True:
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
                repeat_test = ''
                for item in test.item_list:
                    repeat_test += str(item)
                repeat_test += str(test.elevator)
                if repeat_test in previous_positions:
                    legal = False
                if legal == True:
                    legal_next_steps.append(test)


        temporary = ''
        for item in position.item_list:
            temporary += str(item)
        temporary += str(position.elevator)
        previous_positions.append(temporary)

    current_move_positions = legal_next_steps
    step_number += 1
