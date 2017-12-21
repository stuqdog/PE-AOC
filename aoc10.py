import re

bots = {}
output = {}
delete_orders = []
delete_entry = 0

with open("aoc10.txt") as f:
    instructions = [line.strip().split() for line in f]

def main(instructions):
    for order in instructions:

        if order[0] == 'value':
            if order[5] in bots:
                bots[order[5]].append(int(order[1]))
            else:
                bots[order[5]] = [int(order[1])]
        else:
            for i, bot in enumerate([order[1], order[6], order[11]]):
                if order[5*i] != 'bot':
                    output[bot] = []
                elif bot not in bots:
                    bots[bot] = []

    p_one, p_two = 0, 0
    while True:
        for order in instructions:
            if order[0] == 'bot' and len(bots[order[1]]) == 2:
                if order[5] == 'bot':
                    bots[order[6]].append(min(bots[order[1]]))
                else:
                    output[order[6]].append(min(bots[order[1]]))
                if order[10] == 'bot':
                    bots[order[11]].append(max(bots[order[1]]))
                else:
                    output[order[11]].append(max(bots[order[1]]))
                if sorted(bots[order[1]]) == [17, 61]:
                    p_one = order[1]
                bots[order[1]] = []
            if len(output['0']) == len(output['1']) == len(output['2']) == 1:
                p_two = output['0'][0] * output['1'][0] * output['2'][0]
            if p_one and p_two:
                return p_one, p_two


one, two = main(instructions)
print("Part one: {}".format(one))
print("Part two: {}".format(two))
