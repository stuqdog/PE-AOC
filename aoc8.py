def grid_gen(grid):
    for line in grid:
        for c in line:
            yield(c)

with open('aoc8.txt') as f:
    instructions = [line.strip().split() for line in f]

grid = []
for row in range(6):
    new_row = []
    for column in range(50):
        new_row.append(' ')
    grid.append(new_row)

for line in instructions:
    if line[0] == "rect":
        x, y = map(int, line[1].split('x'))
        for row in range(y):
            for column in range(x):
                grid[row][column] = '*'
    elif line[1] == 'row':
        row = int(line[2].split('=')[1])
        shift = int(line[4])
        grid[row] = grid[row][-shift:] + grid[row][:-shift]
    elif line[1] == 'column':
        column = int(line[2].split('=')[1])
        shift = int(line[4])
        new = [grid[i][column] for i in range(6)]
        new = new[-shift:] + new[:-shift]
        for i in range(6):
            grid[i][column] = new[i]

print(sum(1 for c in grid_gen(grid) if c == '*'))
for row in grid:
    print(''.join(row))
