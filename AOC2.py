with open('aoc2.txt') as f:
    instructions = [line.strip() for line in f]


rule = {'U': (0, -1), 'L': (-1, 0), 'R': (1, 0), 'D': (0, 1)}
x, y = 1, 1
solution = ''
# Part one:
# layout = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# part two:
layout = [[0, 0, 1, 0, 0],
          [0, 2, 3, 4, 0],
          [5, 6, 7, 8, 9],
          [0, 'A', 'B', 'C', 0],
          [0, 0, 'D', 0, 0]]

for i in instructions:
    for c in i:
        # For part one, change range to 3
        if x + rule[c][0] in range(5) and y + rule[c][1] in range(5) and (
                layout[y + rule[c][1]][x + rule[c][0]] != 0):
            x, y = x + rule[c][0], y + rule[c][1]
    solution += str(layout[y][x])
print(solution)
