def part_one(instr):
    puzzle = [c for c in 'abcdefgh']
    for line in instr:
        if line[0] == "swap":
            if line[1] == 'position':
                a, b = int(line[2]), int(line[5])
            else:
                a, b = puzzle.index(line[2]), puzzle.index(line[5])
            puzzle[a], puzzle[b] = puzzle[b], puzzle[a]
        elif line[0] == 'rotate':
            if line[1] == 'left':
                a = int(line[2])
            elif line[1] == 'right':
                a = -int(line[2])
            elif line[1] == 'based':
                a = puzzle.index(line[6])
                a += 2 if a >= 4 else 1
                a %= 8
                a = -a
            puzzle = puzzle[a:] + puzzle[:a]
        elif line[0] == 'reverse':
            a, b = int(line[2]), int(line[4])+1
            puzzle = puzzle[:a] + puzzle[a:b][::-1] + puzzle[b:]
        elif line[0] == 'move':
            a, b = puzzle[int(line[2])], int(line[5])
            del puzzle[puzzle.index(a)]
            puzzle.insert(b, a)

    return ''.join(puzzle)

def part_two(instr):
    puzzle = [c for c in 'fbgdceah']
    instr = list(reversed(instr))
    based_conver = {1: 1, 3: 2, 5: 3, 7: 4, 2: 6, 4: 7, 6: 0, 0: 1}
    for line in instr:
        if line[0] == "swap":
            if line[1] == 'position':
                a, b = int(line[2]), int(line[5])
            else:
                a, b = puzzle.index(line[2]), puzzle.index(line[5])
            puzzle[a], puzzle[b] = puzzle[b], puzzle[a]
        elif line[0] == 'rotate':
            if line[1] == 'left':
                a = -int(line[2])
            elif line[1] == 'right':
                a = int(line[2])
            elif line[1] == 'based':
                a = puzzle.index(line[6])
                a = based_conver[a]
            puzzle = puzzle[a:] + puzzle[:a]
        elif line[0] == 'reverse':
            a, b = int(line[2]), int(line[4])+1
            puzzle = puzzle[:a] + puzzle[a:b][::-1] + puzzle[b:]
        elif line[0] == 'move':
            a, b = puzzle[int(line[5])], int(line[2])
            del puzzle[puzzle.index(a)]
            puzzle.insert(b, a)

    return ''.join(puzzle)

with open('aoc21.txt') as f:
    instr = [line.strip().split() for line in f]
print(part_one(instr))
print(part_two(instr))
