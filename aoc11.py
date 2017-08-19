from sys import exit


def legality_check(item_floor):
    """This checks to see if a state is legal, and returns False if not"""
    for x in range(0, 10, 2):
        if (item_floor[x] != item_floor[x + 1]):
            if (item_floor[x] in [item_floor[1], item_floor[3],
                  item_floor[5], item_floor[7], item_floor[9]]):
                return False
    return True


# starting_position and object_names entries correlate to one another.

object_names = ['th_chip', 'th_gen', 'pl_chip', 'pl_gen', 'st_chip',
                'st_gen', 'pr_chip', 'pr_gen', 'ru_chip', 'ru_gen']
starting_position = [1, 1, 2, 1, 2, 1, 3, 3, 3, 3, 1]
current_move_positions = [starting_position]
previous_positions = [starting_position]
step = 0
cache_delete = [1, 0, 0]


while step < 12:

    print "Steps: %d. States checked: %d." % (
                 step, len(previous_positions))
    legal_next_steps = []
    for position in iter(current_move_positions):
        success = True
        # check to see if any given position is a winner.
        for item in position:
            if item != 4:
                success = False
                break
        if success == True:
            print "Success! Total number of steps is %d" % step
            exit()


        movable_object_list = []
        duo_object_temp_storage = []

        for x in xrange(0, 10):
            if position[x] == position[10]:
                movable_object_list.append(object_names[x])

        for x in xrange(0, len(movable_object_list)):
            for y in xrange(x + 1, len(movable_object_list)):
                if (movable_object_list[x].rstrip("chipgen")
                        == movable_object_list[y].rstrip("chipgen") or
                        movable_object_list[x].lstrip("thplsru")
                        == movable_object_list[y].lstrip("thplsru")):
                    duo = movable_object_list[x] + " " + movable_object_list[y]
                    duo_object_temp_storage.append(duo)

        for item in duo_object_temp_storage:
            movable_object_list.append(item)


# Legal moves going up. If elevator == 4 then we're already at the top.
        if position[10] < 4:
            for item in movable_object_list:

                new_layout = position[:]

                for x in xrange(0, 10):
                    if object_names[x] in item:
                        new_layout[x] += 1

                new_layout[10] += 1


                legal = legality_check(new_layout)

                if legal == True and new_layout not in previous_positions:
                    legal_next_steps.append(new_layout)
                    previous_positions.append(new_layout)


# Legal moves going down. If elevator == 1 then we're already at bottom floor.
        if position[10] > 1:
            for item in movable_object_list:

                new_layout = position[:]

                for x in xrange(0, 10):
                    if object_names[x] in item:
                        new_layout[x] -= 1

                new_layout[10] -= 1

                legal = legality_check(new_layout)

                if legal == True and new_layout not in previous_positions:
                    legal_next_steps.append(new_layout)
                    previous_positions.append(new_layout)


    current_move_positions = legal_next_steps
    step += 1
    cache_delete[2] = cache_delete[1]
    cache_delete[1] = cache_delete[0]
    cache_delete[0] = len(legal_next_steps)
    previous_positions = previous_positions[cache_delete[2]:]
