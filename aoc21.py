from sys import exit
import re

current_value = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
turn = 0

def find_value(input_value, line):

    new_value = input_value[:]

    rule = re.match("swap letter (.) with letter (.)", line, re.I)
    if rule:
        for i, c in enumerate(input_value):
            if c == rule.group(1):
                new_value[i] = rule.group(2)
            elif c == rule.group(2):
                new_value[i] = rule.group(1)
        return new_value

    rule = re.match("swap position (.) with position (.)", line, re.I)
    if rule:
        new_value[int(rule.group(1))] = input_value[int(rule.group(2))]
        new_value[int(rule.group(2))] = input_value[int(rule.group(1))]
        return new_value

    rule = re.match("rotate (left|right) (.) steps*", line, re.I)
    if rule:
        if rule.group(1) == "left":
            for x in xrange(0, 8):
                new_value[x] = input_value[(x + int(rule.group(2))) % 8]
            return new_value

        elif rule.group(1) == "right":
            for x in xrange(8, 16):
                new_value[x % 8] = input_value[(x - int(rule.group(2))) % 8]
            return new_value

    rule = re.match("rotate based on position of letter (.)", line, re.I)
    if rule:
        rotations = 1
        for i, c in enumerate(input_value):
            if c == rule.group(1):
                rotations += i
        if rotations > 4:
            rotations += 1
        for x in xrange(8, 16):
            new_value[x % 8] = input_value[(x - rotations) % 8]
        return new_value

    rule = re.match("reverse positions (.) through (.)", line, re.I)
    if rule:
        reverse_start = int(rule.group(1))
        reverse_end = int(rule.group(2))
        #Add here because we want to be reverse to be inclusive on both ends,
        #but our range will ignore the last value
        reverse_total = reverse_end - reverse_start + 1
        if reverse_total < 0:
            reverse_total += 8
        for x in xrange(0, reverse_total):
            new_value[(reverse_start + x) % 8] = (
                      input_value[(reverse_end - x) % 8])
        return new_value

    rule = re.match("move position (.) to position (.)", line, re.I)
    if rule:
        move_from = int(rule.group(1))
        move_to = int(rule.group(2))

        placeholder = input_value[:move_from]
        placeholder += input_value[move_from + 1:]

        new_value = placeholder[:move_to]
        new_value.append(input_value[move_from])
        new_value += placeholder[move_to:]
        return new_value

    print "Something has gone wrong here"
    print new_value
    exit()

with open("aoc21.txt") as f:
    for line in f:
        current_value = find_value(current_value, line)


solution = ''
for c in current_value:
    solution += c
print solution
