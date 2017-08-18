from sys import exit


def add_if_legal(item_floor):
    """This checks to see if a state is legal, and returns False if not"""
    for x in range(0, 10, 2):
        if (item_floor[x] != item_floor[x + 1]):
            if (item_floor[x] in [item_floor[y] for y in range(1,10,2)]):
                return
    if item_floor not in previous_positions:
        legal_next_steps.append(item_floor)
        previous_positions.append(item_floor)



# starting_position and object_names entries correlate to one another.

object_names = ['th_chip', 'th_gen', 'pl_chip', 'pl_gen', 'st_chip',
                'st_gen', 'pr_chip', 'pr_gen', 'ru_chip', 'ru_gen']
starting_position = [1, 1, 2, 1, 2, 1, 3, 3, 3, 3, 1]
current_move_positions = [starting_position]
previous_positions = [starting_position]
step = 0

while True:

    print "Steps: %d. States checked: %d." % (
                 step, len(previous_positions))
    legal_next_steps = []

    for position in current_move_positions:
        if all(floor == 4 for floor in position):
            print "Success! Total number of steps is %d" % step
            print position
            exit()


        movable_object_list = []
        duo_object_temp_storage = []
        single_item_moved_layouts = []

        for x in xrange(0, 10):
            if position[x] == position[10]:
                movable_object_list.append(x)

                if position[x] < 4:
                    new_layout = position[:]
                    new_layout[x] += 1
                    new_layout[10] += 1
                    add_if_legal(layout)

                if position[x] > 1:
                    new_layout = position[:]
                    new_layout[x] -= 1
                    new_layout[10] -= 1
                    add_if_legal(layout)

# Note to self: we can probably make some slight efficiency gains here.
# if a duo consists of a chip and a non-matching gen, we know right away it's
# not legal.
        for i, item in enumerate(movable_object_list):
            for y in movable_object_list[i:]:
                if position[10] < 4:
                    new_layout = position[:]
                    new_layout[x] += 1
                    new_layout[y] += 1
                    new_layout[10] += 1
                    add_if_legal(new_layout)

                if position[10] > 1:
                    new_layout = position[:]
                    new_layout[x] -= 1
                    new_layout[y] -= 1
                    new_layout[10] -= 1
                    add_if_legal(new_layout)
                

    current_move_positions = legal_next_steps
    step += 1
