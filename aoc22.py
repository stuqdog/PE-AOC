import re

nodes = []
solution = 0


class Node(object):

    def __init__(self, name, used, available):
        self.name = name
        self.used = used
        self.available = available


with open("aoc22.txt") as f:
    for line in f:
        stats = re.match("(\S*) \s*(\d*)T \s*(\d*)T \s*(\d*)T", line, re.I)
        if stats:
            nodes.append(Node(stats.group(1), stats.group(3), stats.group(4)))


for i, node in enumerate(nodes):
    for second_node in nodes[i + 1:]:
        if int(node.used) < int(second_node.available) and int(node.used) != 0:
            solution += 1
        if (int(node.available) > int(second_node.used)
                and int(second_node.used) != 0):
            solution += 1

print solution
