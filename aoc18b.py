def find_tile_type(tile):
    if tile == 0:
        return rows[-1][1]

    elif tile == len(start_line) - 1:
        return rows[-1][-2]

    elif rows[-1][tile - 1] != rows[-1][tile + 1]:
        return '^'
    else:
        return '.'


with open("aoc18.txt") as f:
    start_line = f.readline().strip()
rows = [list(start_line)]
solution = 0

for x in xrange(0, 399999):
    new_row = []
    for y in xrange(0, len(start_line)):
        new_tile = find_tile_type(y)
        if new_tile == '.':
            solution += 1
        new_row.append(new_tile)
    rows.append(new_row)

print solution
