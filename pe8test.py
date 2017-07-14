# This shit don't make no sense. Figure out why it's doing what it's
# doing. Figure out how git works so you can ask Matt about it

from sys import argv

script, text = argv

solution = 1
full_number = " "

with open(text) as f:
    for line in f:
        full_number += line.rstrip("\n")

full_num = full_number.lstrip(" ")

for x in range(0, 13):
    current_value = full_num[x]
    solution *= int(current_value)

for x in range(13, 1000):
    check = 1
    for y in range(0, 13):
        current_value = full_num[x - y]
        check *= int(current_value)
    if check > solution:
        solution = check


print full_num
print solution





# this seems to convert num_list into a string, rather than a single object?
# No. it's just reading the first entry in the set, which happens to be the
# only entry because we got rid of linebreaks.
# solution if we don't want to do this would be, number = " ". then, for x
# in range(0, # of lines), number += line. Then run the formula, skipping the
# first character (which is a " ")
# better yet (if it works), number = None. Then if x = 0, number = line, else,
# number += line.


#for x in range(0, 13):
#    current_value = number[x]
#    solution *= int(current_value)

#for x in range(13, 1000):
#    check = 1
#    for y in range(0, 13):
#        current_value = number[x - y]
#        check *= int(current_value)
#    if check > solution:
#        solution = check
#
#print solution
