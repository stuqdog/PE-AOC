from collections import Counter

with open('aoc6.txt') as f:
    instr = [line.strip() for line in f]

print(''.join([Counter([line[x] for line in instr]).most_common()[0][0] for x in range(8)]))
print(''.join([Counter([line[x] for line in instr]).most_common()[-1][0] for x in range(8)]))
