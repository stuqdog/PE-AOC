# 1. Okay, so first we need to create an array. A list of lists of numbers.
# 2. Find out the theoretical highest possible number.
#
# 3. So here's the question: breadth first or depth first?
#   If we do depth first, then we just find a route that's all of the [0] entries.
#   Then, we look at other paths, and reject them if, after taking all the theoretical
#   highest entries for the remaining numbers, we are still below our current high point.
#   Then we iterate thorugh, and get the highest number.
#   This seems slow, though. If we get unlucky we could still be doing a frankly
#   ridiculous number of calculations. Let's try breadth first instead, then.
#
# 4. We don't actually need to find the theoretical highest possible number. We need
#    a class, Path. each entry on Path will have total and current entry. Then we create
#    new entries, and by looking forward (so if current entry is 3, e.g., we could add
#    either 3 or 4 to make a new Path).
#    Once we've done that, we sort the list by total, starting with the biggest.
#    Then, we go through the list. If entry not in [biggest], add entry to biggest.
#     if entry is in biggest, then delete the current entry.  and delete all entries
#     except the highest total valued one for each entry.


class Path(object):

    def __init__(self, total, entry):
        self.total = total
        self.entry = entry

triangle = []
with open("pe67.txt") as f:

    for line in f:
        new_line = map(int, line.strip().split(' '))
        triangle.append(new_line)

first_entry = Path(triangle[0][0], 0)
positions_to_test = [first_entry]

for x in xrange(len(triangle) - 1):
    print x
    next_row_positions = []
    for i, position in enumerate(positions_to_test):
        new_position = Path(position.total + triangle[x + 1][i], i)
        next_row_positions.append(new_position)

        new_position = Path(position.total + triangle[x + 1][i + 1], i + 1)
        next_row_positions.append(new_position)

    biggest_at_position = {}
    positions_to_test = []
    next_row_positions = sorted(next_row_positions,
                         key=lambda position: position.total, reverse=True)
    for position in next_row_positions:
        if position.entry not in biggest_at_position:
            biggest_at_position[position.entry] = position.total
            positions_to_test.append(position)

    positions_to_test = sorted(positions_to_test,
                               key=lambda position: position.entry)


positions_to_test = sorted(positions_to_test,
                    key=lambda position: position.total, reverse=True)

print positions_to_test[0].total
