instructions = "L5, R1, L5, L1, R5, R1, R1, L4, L1, L3, R2, R4, L4, L1, L1, R2, R4, R3, L1, R4, L4, L5, L4, R4, L5, R1, R5, L2, R1, R3, L2, L4, L4, R1, L192, R5, R1, R4, L5, L4, R5, L1, L1, R48, R5, R5, L2, R4, R4, R1, R3, L1, L4, L5, R1, L4, L2, L5, R5, L2, R74, R4, L1, R188, R5, L4, L2, R5, R2, L4, R4, R3, R3, R2, R1, L3, L2, L5, L5, L2, L1, R1, R5, R4, L3, R5, L1, L3, R4, L1, L3, L2, R1, R3, R2, R5, L3, L1, L1, R5, L4, L5, R5, R2, L5, R2, L1, L5, L3, L5, L5, L1, R1, L4, L3, L1, R2, R5, L1, L3, R4, R5, L4, L1, R5, L1, R5, R5, R5, R2, R1, R2, L5, L5, L5, R4, L5, L4, L4, R5, L2, R1, R5, L1, L5, R4, L3, R4, L2, R3, R3, R3, L2, L2, L2, L1, L4, R3, L4, L2, R2, R5, L1, R2".split(', ')

directions = {0: 0, 1: 0, 2: 0, 3: 0}
direction, curr_x, curr_y = 0, 0, 0
solve_two = False
previous = {}
two_orders = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for x in instructions:
    if x[0] == 'L':
        direction -= 1
    else:
        direction += 1
    directions[direction % 4] += int(x[1:])
    if solve_two == False:
        for y in range(int(x[1:])):
            curr_x += two_orders[direction % 4][0]
            curr_y += two_orders[direction % 4][1]

            if (curr_x, curr_y) in previous:
                print(abs(curr_x) + abs(curr_y))
                solve_two = True
            else:
                previous[(curr_x, curr_y)] = 1

print(abs(directions[0] - directions[2]) + abs(directions[1] - directions[3]))
