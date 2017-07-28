total = 0

with open("pe13.txt") as f:
    for line in f:
        total += int(line)

total = str(total)

for x in range(0, 10):
    print total[x],
