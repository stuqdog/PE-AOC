# random encounter program
# write initial section: giving options about terrain, etc
# write terrain-specific sections, give option to change from night to day, etc.
# build in option to move directly from somewhere to home, or to forest,
# or to plains, etc.

#TO DO: Convert this into classes. We can make a terrain class, a combat class,
#etc. etc. Could be cleaned up nicely.
    # Learn Regex.
    # Use classes and regex to create a clean combat option.


import random
import string
import re
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
      4. Plains
      5. Miscellaneous (currently, the bathhouse)"""
    while True:
        answer_t = raw_input("> ")
        if answer_t in ["1", "2", "3", "4", "5"]:
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
    elif answer_t == "5":
        bathhouse()


def urban():
    with open('urban.txt') as f:
        i = len(f.readlines())

    roll = random.randint(1, i)

    with open('urban.txt') as f:
        for x in range(1, roll + 1):
            result = f.readline().strip("\n")

    print_num = True

    entry = re.match(r'(\d*)d(\d*) (.*?),', result, re.I)
    if entry:
        die_num = int(entry.group(1))
        die_size = int(entry.group(2))
        encounter = entry.group(3)
    if not entry:
        entry = re.match(r'(\d*) (.*?), ', result, re.I)
        if entry:
            die_num = int(entry.group(1))
            die_size = 1
            encounter = entry.group(2)
    if not entry:
        entry = re.match(r'(.*?), ', result, re.I)
        print_num = False
        encounter = entry.group(1)
        die_num, die_size = 1, 1

    encounter_number = 0
    for r in range(0, int(die_num)):
        encounter_number += random.randint(1, int(die_size))

    if print_num == True:
        print encounter_number, result.lstrip("1234567890d ")
    else:
        print result
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


def bathhouse():
    with open('bathhouse.txt') as f:
        i = len(f.readlines())

    roll = random.randint(1, i)

    with open('bathhouse.txt') as f:
        for x in range(1, roll + 1):
            result = f.readline().strip("\n")

    print_num = True

    entry = re.match(r'(\d*)d(\d*) (.*?),', result, re.I)
    if entry:
        die_num = int(entry.group(1))
        die_size = int(entry.group(2))
        encounter = entry.group(3)
    if not entry:
        entry = re.match(r'(\d+) (.*?), ', result, re.I)
        if entry:
            die_num = int(entry.group(1))
            die_size = 1
            encounter = entry.group(2)
    if not entry:
        print_num = False
        entry = re.match(r'(.*?), ', result, re.I)
        encounter = entry.group(1)
        die_num, die_size = 1, 1

    encounter_number = 0
    for r in range(0, int(die_num)):
        encounter_number += random.randint(1, int(die_size))
    if print_num == True:
        print encounter_number, result.lstrip("1234567890d ")
    else:
        print result
    bathhouse_end()


def bathhouse_end():
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
        bathhouse_end()
    else:
        bathhouse()




def forest():
    print "Forest TK"
def jungle():
    print "Jungle TK"
def plains():
    print "Plains TK"



def combat():
    # We need to, when going to combat from an encounter, return the result from
    # that encounter. make that the template for combat, but let us replace it
    # if we want. Then use classes to turn it into enemies, and put those classes
    # occurrences in a dictionary. class features are HP, damage, AC, to hit,
    # maybe spells, for casters, maybe a way to capture unique abilities?
    # then we have combat simulation for those things, when their HP is reduced
    # to zero, we delete them from our combat dictionary. Learn regex to cleanly
    # reduce encounter results into numbers and strings for the actual encounter
    print "Combat TK"


home()
