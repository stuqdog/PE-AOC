with open('aoc9.txt') as f:
    puzzle = [line.strip() for line in f][0]

def part_one(puzzle):
    solution = 0
    determine_multiplier = False
    multiplier = ''
    add_amount = 1
    time = 0
    for c in puzzle:
        if c == "(" and time == 0:
            determine_multiplier = True
        elif c == ')' and time == 0:
            if determine_multiplier == True:
                determine_multiplier = False
                time, add_amount = map(int, multiplier.split('x'))
                time += 1
        elif determine_multiplier:
            multiplier += c
        else:
            solution += add_amount
        if time:
            time -= 1
            if time == 0:
                add_amount = 1
                multiplier = ''
    return solution

def part_two(puzzle):
    solution = 0
    multipliers = []
    multiplier = ''
    total_multiplier = 1
    determine_multiplier = False

    for c in puzzle:
        if c == "(":
            determine_multiplier = True
        elif c == ')':
            determine_multiplier = False
            time, add_amount = map(int, multiplier.split('x'))
            multipliers.append([time, add_amount])
            total_multiplier *= add_amount
            multiplier = ''
        elif determine_multiplier:
            multiplier += c
        else:
            solution += total_multiplier

        for i in multipliers:
            if i[0] == 0:
                total_multiplier //= i[1]
            i[0] -= 1
    return solution

print(part_one(puzzle))
print(part_two(puzzle))
