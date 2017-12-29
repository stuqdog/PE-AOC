with open("aoc20.txt") as f:
    instr = [list(map(int, line.strip().split('-'))) for line in f]

instr = sorted(instr, key=lambda x: x[0])

def part_one(instr):
    for i, x in enumerate(instr):
        if x[1] + 1 < instr[i+1][0]:
            return x[1] + 1

def part_two(instr):
    blocked_ip = 0
    solution = 0
    for i in range(len(instr) - 1):
        blocked_ip = max(blocked_ip, instr[i][1] + 1)
        if blocked_ip < instr[i+1][0]:
            solution += (instr[i+1][0] - blocked_ip)
    return solution

print(part_one(instr))
print(part_two(instr))
