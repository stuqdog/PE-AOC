time = 0
lapsed_positions = [[11, 13], [17, 17], [20, 19], [5, 7], [5, 5], [7, 3]]

while True:
    if all(position[0] % position[1] == 0 for position in lapsed_positions):
        print time
        break
    time += 1
    for position in lapsed_positions:
        position[0] += 1
