from sys import argv
import string

script, text = argv
numbers = string.digits

# setting each row as its own list so that we can put them in the larger list
# grid, thus allowing us to call specific lights by both their X and Y
# coordinates as grid[y][x]
row_zero = []
row_one = []
row_two = []
row_three = []
row_four = []
row_five = []

grid = [row_zero, row_one, row_two, row_three, row_four, row_five]

# placeholder as a dictionary is a way of copying the value of the
# row/column being rotated without equating to grid directly, since doing
# so causes placeholder to also be equal to the row lists. dictionary rather
# than a list, because it's easier to create new values inside it and we
# don't need it to run in order.
placeholder = {}

# quickly fill out each row with 50 blank lights
for y in range(0, 6):
    for x in range(0, 50):
        grid[y].append(" ")


with open(text) as f:
    for line in f:
        if "rect" in line:
            rect_size = line.strip("rect \n")
            rect_x = rect_size.rstrip(numbers)
            rect_x = int(rect_x.rstrip("x"))
            rect_y = rect_size.lstrip(numbers)
            rect_y = rect_y.rstrip("\n")
            rect_y = int(rect_y.lstrip("x"))
            for y in range(0, rect_y):
                for x in range(0, rect_x):
                    grid[y][x] = "*"
        elif "rotate row" in line:
            rotate_x = line.strip("rotate row y=\n")
            row = rotate_x.rstrip(numbers)
            row = int(row.rstrip(" by "))
            shift = rotate_x.lstrip(numbers)
            shift = int(shift.lstrip(" by "))
            for x in range(0, 50):
                placeholder[x] = grid[row][x]
            for x in range(0, 50):
                grid[row][x] = placeholder[(x + 50 - shift) % 50]
        elif "rotate column" in line:
            rotate_y = line.strip("rotate column x= \n")
            column = rotate_y.rstrip(numbers)
            column = int(column.rstrip(" by "))
            shift = rotate_y.lstrip(numbers)
            shift = int(shift.lstrip(" by "))
            for x in range(0, 6):
                placeholder[x] = grid[x][column]
            for x in range(0, 6):
                grid[x][column] = placeholder[(x + 6 - shift) % 6]

for x in range(0, 6):
    print ''.join(grid[x])
