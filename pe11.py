grid = {}
solution = 0

with open("pe11.txt") as f:
    x = 0
    for line in f:
        grid[x] = []
        this_line = line.strip("\n")
        this_line = this_line.split(" ")
        for i in range(0, len(this_line)):
            grid[x].append(this_line[i])
        x += 1

column_num = len(grid[0])

# this segment does horizontal checks
for row in grid:
    for x in range(3, column_num):
        check = (int(grid[row][x]) * int(grid[row][x - 1])
        * int(grid[row][x - 2]) * int(grid[row][x - 3]))
        if check > solution:
            solution = check
            num_1, num_2, num_3, num_4 = (grid[row][x], grid[row][x - 1],
            grid[row][x - 2], grid[row][x - 3])

# this segment does vertical checks
for x in range(0, column_num):
    for y in range(3, len(grid)):
        check = (int(grid[y][x]) * int(grid[y - 1][x])
         * int(grid[y - 2][x]) * int(grid[y - 3][x]))
        if check > solution:
            solution = check
            num_1, num_2, num_3, num_4 = (grid[y][x], grid[y - 1][x],
            grid[y - 2][x], grid[y - 3][x])

#this segment does diagonal checks, top left to bottom right
for x in range(0, column_num - 3):
    for y in range(0, len(grid) - 3):
        check = (int(grid[y][x]) * int(grid[y + 1][x + 1])
        * int(grid[y + 2][x + 2]) * int(grid[y + 3][x + 3]))
        if check > solution:
            solution = check
            num_1, num_2, num_3, num_4 = (grid[y][x], grid[y + 1][x + 1],
            grid[y + 2][x + 2], grid[y + 3][x + 3])

# this segment does diagonal checks, top right to bottom left
for x in range(3, column_num):
    for y in range(0, len(grid) - 3):
        check = (int(grid[y][x]) * int(grid[y + 1][x - 1])
        * int(grid[y + 2][x - 2]) * int(grid[y + 3][x - 3]))
        if check > solution:
            solution = check
            num_1, num_2, num_3, num_4 = (grid[y][x], grid[y + 1][x - 1],
            grid[y + 2][x - 2], grid[y + 3][x - 3])

print solution
print num_1, num_2, num_3, num_4
