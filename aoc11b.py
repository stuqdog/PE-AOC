from sys import exit


def add_if_legal(item_floor):
    """This checks to see if a state is legal, and returns False if not"""
    for x in range(0, 14, 2):
        if (item_floor[x] != item_floor[x + 1]):
            if item_floor[x] in (item_floor[y] for y in range(1, 14, 2)):
                return
    if item_floor not in previous_positions:
        legal_next_steps.append(item_floor)
        previous_positions.append(item_floor)


# starting_positions and object_names entries correlate to one another.
# object_names = ['th_chip', 'th_gen', 'pl_chip', 'pl_gen', 'st_chip',
#                 'st_gen', 'pr_chip', 'pr_gen', 'ru_chip', 'ru_gen',
#                 'el_chip', 'el_gen', 'di_chip', 'di_gen']

starting_positions = [1, 1, 2, 1, 2, 1, 3, 3, 3, 3, 1, 1, 1, 1, 1]
current_move_positions = [starting_positions]
previous_positions = [starting_positions]
step = 0
cache_delete = [1, 0, 0]

while True:

    print "Steps: %d. States checked: %d." % (step,
                                              len(previous_positions))
    legal_next_steps = []

    for position in iter(current_move_positions):
        # check to see if any given position is a winner.
        if all(floor == 4 for floor in position):
            print "Success! Total number of steps is %d" % step
            exit()


        movable_object_list = []
        # duo_object_temp_storage = []

        for x in xrange(0, 14):
            if position[x] == position[14]:
                movable_object_list.append(x)
                # movable_object_list.append(object_names[x])
                if position[x] < 4:
                    new_layout = position[:]
                    new_layout[x] += 1
                    new_layout[14] += 1
                    add_if_legal(new_layout)
                if position[x] > 1:
                    new_layout = position[:]
                    new_layout[x] -= 1
                    new_layout[14] -= 1
                    add_if_legal(new_layout)

        for x, item in enumerate(movable_object_list):
            for y in movable_object_list[x+1:]:
                if y - item != 1 and (y - item) % 2 != 0:
                    pass
                else:
                    if position[14] < 4:
                        new_layout = position[:]
                        new_layout[item] += 1
                        new_layout[y] += 1
                        new_layout[14] += 1
                        add_if_legal(new_layout)

                    if position[14] > 1:
                        new_layout = position[:]
                        new_layout[item] -= 1
                        new_layout[y] -= 1
                        new_layout[14] -= 1
                        add_if_legal(new_layout)

        # for x in xrange(0, len(movable_object_list)):
        #     for y in xrange(x + 1, len(movable_object_list)):
        #         if (movable_object_list[x].rstrip("chipgen")
        #                 == movable_object_list[y].rstrip("chipgen") or (
        #                 movable_object_list[x].lstrip("thplsruedi")
        #                 == movable_object_list[y].lstrip("thplsruedi"))):
        #             duo = movable_object_list[x] + " " + movable_object_list[y]
        #             duo_object_temp_storage.append(duo)
        #
        # for item in duo_object_temp_storage:
        #     movable_object_list.append(item)



# Legal moves going up. If elevator == 4 then we're already at the top.
#         if position[14] < 4:
#             for item in movable_object_list:
#
#                 new_layout = position[:]#list(position)
#                 # for i in position:
#                 #     new_layout.append(i)
#
#                 for x in xrange(0, len(object_names)):
#                     if object_names[x] in item:
#                         new_layout[x] += 1
#
#                 new_layout[14] += 1
#                 legal = legality_check(new_layout)
#
#                 if legal == False:
#                     pass
#                 elif new_layout not in previous_positions:
#                     legal_next_steps.append(new_layout)
#                     previous_positions.append(new_layout)
#
#
# # Legal moves going down. If elevator == 1 then we're already at bottom floor.
#         if position[14] > 1:
#             for item in movable_object_list:
#
#                 new_layout = position[:]#list(position)
#                 # for i in position:
#                 #     new_layout.append(i)
#
#                 for x in xrange(0, len(object_names)):
#                     if object_names[x] in item:
#                         new_layout[x] -= 1
#
#                 new_layout[14] -= 1
#                 legal = legality_check(new_layout)
#                 if legal == False:
#                     pass
#                 elif new_layout not in previous_positions:
#                     legal_next_steps.append(new_layout)
#                     previous_positions.append(new_layout)


    current_move_positions = legal_next_steps
    step += 1
    cache_delete[2] = cache_delete[1]
    cache_delete[1] = cache_delete[0]
    cache_delete[0] = len(legal_next_steps)
    previous_positions = previous_positions[cache_delete[2]:]
