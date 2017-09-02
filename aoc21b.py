# Things that need to be swapped
#1. rotate left/right. These should be reversed. so rotate left becomes
    #rotate right, etc.
    #should be done. just reversed the ifs i.e. if right, then do left code
#2. rotate based on position of letter x. need to make it rotate left, not right
    #This seems complicated. How do we know how many times it rotated to ends
    #up where it is now?
        # if 0, then rotate 1 time, end on 1
        # if 1, rotate 2 times, end on 3
        # if 2, then rotate 3 times, end on 5
        # if 3, then rotate 4 times, end on 7
        # if 4, then rotate 6 times, end on 2
        # if 5, then rotate 7 times, end on 4.
        # if 6, then rotate 8 times, end on 6
        # if 7, then rotate 9 times, end on 0. if 2, then 5. if 3, then
        # if our current value is odd: rotate number of times = 1/2 current value + 1
        # if our current value is even, rotate a number of times = 1/2 current value + 5
            # (treat 0 as 8, so we have 9 instead of 5)
    # This is solved too. Make it rotate right, and use rotation values based
    # on the simple rules above.
#3. move position x to y. This should move position y to x.
    #this should be solved. Just swap move_from and move_to values.




from sys import exit
import re

current_value = ['f', 'b', 'g', 'd', 'c', 'e', 'a', 'h']
turn = 0
instructions = []

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
        if rule.group(1) == "right":
            for x in xrange(0, 8):
                new_value[x] = input_value[(x + int(rule.group(2))) % 8]
            return new_value

        elif rule.group(1) == "left":
            for x in xrange(8, 16):
                new_value[x % 8] = input_value[(x - int(rule.group(2))) % 8]
            return new_value

    rule = re.match("rotate based on position of letter (.)", line, re.I)
    if rule:
        rotations = 1
        for i, c in enumerate(input_value):
            # rules for determining where letter started based on where it is
            if c == rule.group(1):
                if i == 0:
                    rotations = 1
                elif i % 2 == 0:
                    rotations = i / 2 + 5
                else:
                    rotations = (i + 1) / 2
        for x in xrange(0, 8):
            new_value[x] = input_value[(x + rotations) % 8]
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
        move_from = int(rule.group(2))
        move_to = int(rule.group(1))

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
        instructions.append(line)

print len(instructions)

for instruction in reversed(instructions):
    #print instruction
    current_value = find_value(current_value, instruction)


solution = ''
for c in current_value:
    solution += c
print solution
