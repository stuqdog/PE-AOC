import string

raw = ""
mode = "add"
length_or_size = "length"
length, size = "", ""
solution = 0
multiplier = 1
buffer_dict = {}
dict_delete = []

# create a string of the text, so we can read it char by char.
with open("aoc9.txt") as f:
    for line in f:
        raw += line

for c in raw:

# this checks if the duration of a multiplier has gone out. if it has, we
# delete that multiplier entry and divide the multiplier_var by the multiplier.

#this needs to be up top so entries don't lose 1 as soon as they enter the dict.
    for entry in buffer_dict:
        buffer_dict[entry] -= 1

    if c != "(" and mode == "add":
        solution += multiplier

# an open bracket means we're in a marker, so the rules change.
    elif c == "(":
        mode = "change_multiplier"

    elif c in string.digits and length_or_size == "length":
        length += c

    elif c == 'x':
        length_or_size = "size"

    elif c in string.digits and length_or_size == "size":
        size += c

# leaving the buffer zone. change back to add mode, reset variables that are
# determined within the buffer, and add the multiplier to our dictionary.
    elif c == ")":
        while size in buffer_dict:
            size += 'a'
        buffer_dict[size] = int(length)
        multiplier *= int(size.strip('a'))
        size, length = "", ""
        mode = "add"
        length_or_size = "length"
    elif c in [" ", "\n"]:
        pass

#this needs to be at the bottom so we don't divide the multiplier before
#we get a chance to add it to our solution
    for entry in buffer_dict:
        if buffer_dict[entry] == 0:
            dict_delete.append(entry)
            multiplier /= int(entry.strip('a'))
    for entry in dict_delete:
        del buffer_dict[entry]
    dict_delete = []

print solution
