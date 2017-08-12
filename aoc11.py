from sys import exit


class Map(object):

    def __init__(self, item_floor):
## item_floor vars: see object_names below. also: elevator at [-1] position.
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

# starting_positions and object_names entries correlate to one another.

object_names = ['th_chip', 'th_gen', 'pl_chip', 'pl_gen', 'st_chip',
                'st_gen', 'pr_chip', 'pr_gen', 'ru_chip', 'ru_gen']
starting_positions = [1, 1, 2, 1, 2, 1, 3, 3, 3, 3, 1]
current_move_positions = [Map(starting_positions)]
previous_positions = [Map(starting_positions)]
step_number = 0
previous_positions = []

while True:

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
            print "Success! Total number of steps is %d" % step_number
            exit()


        movable_object_list = []
        duo_object_temp_storage = []

        for x in xrange(0, 10):
            if position.item_floor[x] == position.item_floor[10]:
                movable_object_list.append(object_names[x])

        for x in xrange(0, len(movable_object_list)):
            for y in xrange(x + 1, len(movable_object_list)):
                duo = movable_object_list[x] + " " + movable_object_list[y]
                duo_object_temp_storage.append(duo)

        for item in duo_object_temp_storage:
            movable_object_list.append(item)


# Legal moves going up. If elevator == 4 then we're already at the top.
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
                    previous_positions.append(new_layout)


# Legal moves going down. If elevator == 1 then we're already at bottom floor.
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
                    previous_positions.append(new_layout)


    current_move_positions = legal_next_steps
    step_number += 1
