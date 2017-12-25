time = 0
lapsed_positions = [[12, 13], [2, 5], [14, 17], [4, 3], [7, 7], [23, 19], [7, 11]]

while True:
    if all(position[0] % position[1] == 0 for position in lapsed_positions):
        print(time)
        break
    time += 1
    for position in lapsed_positions:
        position[0] += 1
