# random encounter program
# write initial section: giving options about terrain, etc
# write terrain-specific sections, give option to change from night to day, etc.
# build in option to move directly from somewhere to home, or to forest,
# or to plains, etc.


import random
import string
from sys import exit




def home():
    print """Welcome to the GM assistant!
What can I assist you with today?
  1. Random encounters
  2. Combat"""

    while True:
        answer = raw_input("> ")
        if answer in ["1", "2"]:
            break
        else:
            print "ERROR: please enter 1 or 2"

    if answer == "1":
        terrain_check()
    elif answer == "2":
        combat()



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
    with open('urban.txt') as f:
        i = len(f.readlines())

    roll = random.randint(1, i)

    with open('urban.txt') as f:
        for x in range(1, roll + 1):
            result = f.readline().strip("\n")


    die_num = " "
    die_size = " "
    for x in range(0, 2):
        if result[x] in string.digits:
            die_num += result[x]
        else:
            die_num = die_num.lstrip()
            break
    die_num = die_num.lstrip()
    find_size = result.lstrip("0123456789")
    find_size = find_size.lstrip("d")
    for x in range(0, 3):
        if find_size[x] in string.digits:
            die_size += find_size[x]
        else:
            die_size = die_size.lstrip()
            break

    encounter_number = 0
    for r in range(0, int(die_num)):
        encounter_number += random.randint(1, int(die_size))

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
        print""" ct: Change terrain
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
