# Read the file. while dup_stats is false, add bits to a string called solution.
#
# if we come across a parenthesis, turn on dup_stats. while duplicate is on, we
# read until we reach a close parenthesis, putting values into dup_length and
# dup_num.
#
# after close parenthesis, we turn off stats, and turn on dup_process.
# while dup_process is on, we print dup_length character dup_num times. Then, turn
# off dup_process.
#
# Rinse and repeat, then add up the length of what we have.
#
# How do we structure the functioning?

import string


dup_num = " "
dup_len = " "
dup_count = 0
dup_string = " "
dup_stats = False
dup_process = False
raw = " "
solution = " "

with open("aoc9.txt") as f:
    for line in f:
        raw += line

raw = raw.strip()

for c in raw:
    if dup_stats == False and dup_process == False:
        dup_num = " "
        dup_len = " "
        dup_string = " "
        dup_count = 0
        dup_stats = False
        dup_process = False
        if c == "(":
            dup_stats = True
        else: solution += c

    if dup_stats == True and dup_process == False:
        if c in string.digits:
            dup_len += c

        elif c == "x":
            dup_process = True

    if dup_stats == True and dup_process == True:
        if c in string.digits:
            dup_num += c
            print dup_num

        elif c == ")":
            dup_stats = False

    if dup_stats == False and dup_process == True:
        # dup_num = dup_num.strip()
        # dup_num = int(dup_num)
        # dup_len = int(dup_len.strip())
        if dup_count < dup_len:
            dup_string += c
            dup_count += 1
        if dup_count == dup_len:
            for x in range(0, dup_num):
                solution += dup_string
            dup_process = False

#print solution
solution = solution.strip()
