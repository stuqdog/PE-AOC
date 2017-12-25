first_row = '.^^..^...^..^^.^^^.^^^.^^^^^^.^.^^^^.^^.^^^^^^.^...^......^...^^^..^^^.....^^^^^^^^^....^^...^^^^..^'
rows = [[True if c == '.' else False for c in first_row]]
solution = sum(1 for c in first_row if c == '.')

for x in range(399999):
    new_row = []
    for y in range(len(first_row)):
        if y == 0:
            new_row.append(rows[x][y+1])
        elif y == 99:
            new_row.append(rows[x][y-1])
        else:
            if rows[x][y-1] == rows[x][y+1]:
                new_row.append(True)
            else:
                new_row.append(False)
    solution += sum(1 for c in new_row if c == True)
    rows.append(new_row)
    if x == 38:
        print("Part one: {}".format(solution))
print("Part two: {}".format(solution))
