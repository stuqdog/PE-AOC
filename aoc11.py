def add_if_legal(item_floor):
    """This checks to see if a state is legal, and returns False if not"""
    for x in range(0, 14, 2):
        if (item_floor[x] != item_floor[x + 1]):
            if item_floor[x] in (item_floor[y] for y in range(1, 14, 2)):
                return
    if str(item_floor) not in previous_positions:
        legal_next_steps.append(item_floor)
        previous_positions[str(item_floor)] = step

starting_position = [1, 1, 2, 1, 2, 1, 3, 3, 3, 3, 1, 1, 1, 1, 1]
# starting_position = [1, 1, 2, 1, 2, 1, 3, 3, 3, 3, 1]
current_move_positions = [starting_position]
previous_positions = {str(starting_position): 0}
step = 0
part_one = False

while part_one == False:

    print("Steps: {}".format(step))
    legal_next_steps = []
    for position in current_move_positions:
        if all(floor == 4 for floor in position):
            print("Part one: {}".format(step))
            part_one = True

        movable_object_list = [x for x in range(14) if position[x] == position[14]]
        if position[14] < 4:
            for x in movable_object_list:
                new = position[:]
                new[x] += 1
                new[14] += 1
                add_if_legal(new)
        if position[14] > 1:
            for x in movable_object_list:
                new = position[:]
                new[x] -= 1
                new[14] -= 1
                add_if_legal(new)


        for x, item in enumerate(movable_object_list):
            for y in movable_object_list[x+1:]:
                if y - item == 1 or (y - item) % 2 == 0:
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

    current_move_positions = legal_next_steps
    step += 1
