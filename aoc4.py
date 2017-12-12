from collections import Counter
import re

with open("aoc4.txt") as f:
    instr = [line for line in f]

alpha = 'abcdefghijklmnopqrstuvwxyz'

solution = 0
for line in instr:
    code, val, key = re.match("(.*)-(\d+)\[(.*)\]", line).groups()
    count = Counter(code)
    sort = sorted(Counter(code), key=str.lower)
    sort = sorted(sort, key=lambda x: Counter(code)[x], reverse=True)
    sort.remove('-')
    check = ''.join(sort[:5])
    if check == key:
        solution += int(val)
        new = ''
        for c in code:
            if c != '-':
                new += alpha[(alpha.index(c) + int(val)) % 26]
        if 'north' in new:
            print(val)
print(solution)
