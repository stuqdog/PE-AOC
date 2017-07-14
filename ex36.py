# random encounter program
# write initial section: giving options about terrain, etc
# write terrain-specific sections, give option to change from night to day, etc.
# build in option to move directly from somewhere to home, or to forest,
# or to plains, etc.

# how to read the random encounter tables? Jump to a specific line?
# I could just read every line from 1 to x where x is target line, and
# then print line. But there's probably a better way to do it than that.
        # Urban uses the above mentioned method. Seems to work fine.
        # Let's start with that and figure out how to print it with random
        # numbers added in.

import random
import string
from sys import exit, argv

script, urban_table = argv#forest_table, plains_table, jungle_table = argv

# these are clunky. Replace with a "with x as y" thing.
# with open(urban_table) as urban_t:
# urban_t = open(urban_table)
#forest_t = open(forest_table)

def home():
    print """Welcome to the GM assistant!
What can I assist you with today?
  1. Random encounters
  2. Combat"""

    while True:
        answer = raw_input("> ")
        if answer in ["1", "2"]:
            break
    #    elif answer == "2":
    #        break
        else:
            print "error, pls enter real answer"
    if answer == "1":
        terrain_check()
    elif answer == "2":
        combat()

#    answer = raw_input("> ")
#    if answer == "1":
#        terrain_check()
#    elif answer == "2":
#        combat()
#    else:
#        home()

def terrain_check():
    print """What kind of terrain are you dealing with?
      1. Urban
      2. Forest
      3. Jungle
      4. Plains"""
    while True:
        answer_t = raw_input("> ")
        if answer_t in ["1", "2", "3", "4"]:
            break
        else:
            print "Error. Please enter a valid response."
    if answer_t == "1":
        urban()
    elif answer_t == "2":
        forest()
    elif answer_t == "3":
        jungle()
    elif answer_t == "4":
        plains()



def urban():
    with open(urban_table) as f:
        i = len(f.readlines())

    roll = random.randint(1, i)

    with open(urban_table) as f:
        for x in range(1, roll + 1):
            result = f.readline()
            die_num = int(result[0])
            die_size = int(result[2])

    encounter_number = 0
    for r in range(0, die_num):
        encounter_number += random.randint(1, die_size)

    print encounter_number, result.lstrip("1234567890d ")
    urban_end()

def urban_end():
    next_step = raw_input("> ")
    if next_step == "ct":
        terrain_check()
    elif next_step == "combat":
        combat()
    elif next_step == "home":
        home()
    elif next_step == "exit":
        exit(0)
    elif next_step == "help":
        print"""ct: Change terrain
combat: combat
home: return home
exit: quit program
anything else: generate new urban encounter"""
        urban_end()
    else:
        urban()









def forest():
    print "Forest TK"
def jungle():
    print "Jungle TK"
def plains():
    print "Plains TK"
def combat():
    print "Combat TK"


home()
