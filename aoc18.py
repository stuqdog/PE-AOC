def find_tile_type(tile):

    if tile in range(0, len(start_line) - 1):
        right = rows[-1][tile + 1]
    else:
        right = "."

    if tile in range(1, len(start_line)):
        left = rows[-1][tile - 1]
    else:
        left = "."

    center = rows[-1][tile]

    if left != right:
        return '^'
    else:
        return '.'


with open("aoc18.txt") as f:
    start_line = f.readline().strip()
print start_line
print len(start_line)
rows = [list(start_line)]

# generate 39 new rows, since the first one is a freebie
for x in range(0, 39):
    new_row = []
    for y in range(0, len(start_line)):
        new_tile = find_tile_type(y)
        new_row.append(new_tile)
    rows.append(new_row)

solution = 0
for row in rows:
    for tile in row:
        if tile == ".":
            solution += 1

print solution
