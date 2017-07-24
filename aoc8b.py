# read the directions, break them up by text.
# once we know right direction, reduce it to the numbers necessary
# for rotate, grid[x][y] = grid_template[x - rotate][y]


from sys import argv
import string

script, text = argv

numbers = string.digits
numbers += "\n"

row_zero = []
row_one = []
row_two = []
row_three = []
row_four = []
row_five = []

grid = [row_zero, row_one, row_two, row_three, row_four, row_five]
grid_record = grid

## grid[a][b] would be the a row, and b column

for y in range(0, 6):
    for x in range(0, 50):
        grid[y].append("_")


with open(text) as f:
    for line in f:
        print grid
        grid_record = grid
        if "rect" in line:
            rect_size = line.lstrip("rect ")
            rect_x = rect_size.rstrip(numbers)
            rect_x = int(rect_x.rstrip("x"))
            rect_y = rect_size.lstrip(numbers)
            rect_y = rect_y.rstrip("\n")
            rect_y = int(rect_y.lstrip("x"))
            for y in range(0, rect_y):
                for x in range(0, rect_x):
                    grid[y][x] = "X"
        elif "rotate row" in line:
            rotate_x = line.lstrip("rotate row y=")
            row = rotate_x.rstrip(numbers)
            row = int(row.rstrip(" by "))
            shift = rotate_x.lstrip(numbers)
            shift = int(shift.lstrip(" by "))
            for x in range(0, 50):
                grid[row][x] = grid_record[row][((x + 50) - shift) % 50]
        elif "rotate column" in line:
            rotate_y = line.lstrip("rotate column x=")
            column = rotate_y.rstrip(numbers)
            column = int(column.rstrip(" by "))
            shift = rotate_y.lstrip(numbers)
            shift = int(shift.lstrip(" by "))
            for x in range(0, 6):
                grid[x][column] = grid_record[(x + 6 - shift) % 6][column]
