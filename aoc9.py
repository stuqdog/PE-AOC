import string

#note: the next 4 vars are all defined below, so defining them here is
#unneccessary, but lets me comment in what purpose they serve.

# number of times a section is duplicated.
dup_number = ""
#number of character in the section remaining to to be duplicated. Ticks down
# as characters are added to dup_string.
dup_len = ""
# the string that gets duplicated
dup_string = ""


stage = "adding"
raw = ""
solution = ""

with open("aoc9.txt") as f:
    for line in f:
        raw += line

for c in raw:

    if stage == "duplicate":
        if int(dup_len) > 0:
            dup_string += c
            dup_len = int(dup_len) - 1
        if dup_len == 0:
            dup_string = dup_string.strip()
            for x in range(0, int(dup_num)):
                solution += dup_string
            stage = "adding"

    elif stage == "dup_num":
        if c in string.digits:
            dup_num += c

        elif c == ")":
            stage = "duplicate"


    elif stage == "dup_len":
        if c in string.digits:
            dup_len += c

        elif c == "x":
            stage = "dup_num"

    elif stage == "adding":
        dup_num = ""
        dup_len = ""
        dup_string = ""
        if c == "(":
            stage = "dup_len"
        else: solution += c

print len(solution)
