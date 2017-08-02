# random encounter program
# write initial section: giving options about terrain, etc
# write terrain-specific sections, give option to change from night to day, etc.
# build in option to move directly from somewhere to home, or to forest,
# or to plains, etc.

#TO DO: Convert this into classes. We can make a terrain class, a combat class,
#etc. etc. Could be cleaned up nicely.
    # Learn Regex.
    # Use classes and regex to create a clean combat option.


from random import randint
import string
import re
from sys import exit
encounter_number = 0



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
        return "terrain_check"
    elif answer == "2":
        return "combat"



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
        return "urban"
        # urban()
    elif answer_t == "2":
        return "forest"
        # forest()
    elif answer_t == "3":
        jungle()
    elif answer_t == "4":
        plains()
    elif answer_t == "5":
        return "bathhouse"
        # bathhouse()


def urban():
    with open('urban.txt') as f:
        i = len(f.readlines())

    roll = randint(1, i)

    with open('urban.txt') as f:
        for x in range(1, roll + 1):
            result = f.readline().strip("\n")

    entry = re.match(r'(\d*)d(\d*) (.*?),', result, re.I)
    if entry:
        die_num = int(entry.group(1))
        die_size = int(entry.group(2))
        encounter = entry.group(3)
    if not entry:
        entry = re.match(r'(\d*) (.*?), ', result, re.I)
        if entry:
            die_num, die_size = int(entry.group(1)), 1
            encounter = entry.group(2)
    if not entry:
        entry = re.match(r'(.*?), ', result, re.I)
        encounter = entry.group(1)
        die_num, die_size = 1, 1

    encounter_number = 0
    for r in range(0, int(die_num)):
        encounter_number += randint(1, int(die_size))

    if encounter_number > 1:
        print encounter_number, (result.lstrip("1234567890d")).lstrip()
    else:
        print (result.lstrip("1234567890d")).lstrip()
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

    roll = randint(1, i)

    with open('bathhouse.txt') as f:
        for x in range(1, roll + 1):
            result = f.readline().strip("\n")

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
        entry = re.match(r'(.*?), ', result, re.I)
        encounter = entry.group(1)
        die_num, die_size = 1, 1

    encounter_number = 0
    for r in range(0, int(die_num)):
        encounter_number += randint(1, int(die_size))

    if encounter_number > 1:
        print encounter_number, (result.lstrip("1234567890d")).lstrip()
    else:
        print (result.lstrip("123456789d")).lstrip()
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

    with open('forest.txt') as f:
        i = len(f.readlines())

    roll = randint(1, i)

    with open('forest.txt') as f:
        for x in range(1, roll + 1):
            result = f.readline().strip("\n")

    # entry = re.match(r'''(\d*)d(\d*) (.*) <(H[D|P]): (\d*), AC: (\d*),
    # damage: (\d*)d(\d*), morale: (\*d)> .*''', result, re.I)
    test = '(\d*)d(\d*) (.*) <(H[D|P]): (\d*), AC: (\d*),'
    test += ' damage: (\d*)d(\d*), morale: (\d*)>,'
    entry = re.match(test, result, re.I)
    if entry:
        die_num = int(entry.group(1))
        die_size = int(entry.group(2))
        encounter = entry.group(3)
        if entry.group(4) == "HP":
            HP = int(entry.group(5))
            HD = None
        elif entry.group(4) == "HD":
            HD = int(entry.group(5))
            HP = None
        AC = entry.group(6)
        damage = [int(entry.group(7)), int(entry.group(8))]
        morale = entry.group(9)


    else: print "ERROR"

    encounter_number = 0
    for r in range(0, int(die_num)):
        encounter_number += randint(1, int(die_size))

    if encounter_number > 1:
        print encounter_number, (result.lstrip("1234567890d")).lstrip()
    else:
        print (result.lstrip("1234567890d")).lstrip()


    while True:
        next_step = raw_input("> ")

        if next_step == "ct":
            return "terrain_check()", None, None, None, None, None, None
        elif next_step == "combat":
            return "combat()", encounter, HD, AC, damage, morale, encounter_number
        elif next_step == "home":
            return "home()", None, None, None, None, None, None
        elif next_step == "exit":
            exit(0)
        elif next_step == "help":
            print""" ct: Change terrain
 combat: combat
 home: return home
 exit: quit program
 anything else: generate new urban encounter"""
    else:
        return "forest()", None, None, None, None, None, None








def jungle():
    print "Jungle TK"
def plains():
    print "Plains TK"



def combat(encounter, HD, AC, damage, morale, encounter_number):
    print encounter, HD, AC, damage, morale, encounter_number
    exit()

    # We need to, when going to combat from an encounter, return the result from
    # that encounter. make that the template for combat, but let us replace it
    # if we want. Then use classes to turn it into enemies, and put those class
    # occurrences in a dictionary. class features are HP, damage, AC, to hit,
    # maybe spells, for casters, maybe a way to capture unique abilities?
    # then we have combat simulation for those things, when their HP is reduced
    # to zero, we delete them from our combat dictionary. Learn regex to cleanly
    # reduce encounter results into numbers and strings for the actual encounter
    HP = 3
    HD = None
    AC = 40
    damage = 5
    morale = 6
    encounter_number = 4
    encounter = "monkey"
    print "Combat TK"
    print encounter_number

    encounter_set = {}
    encounter_counter = 1


    for enemy in range(0, encounter_number):
        if encounter_counter > 1:
            this_enemy = encounter + " %s" % str(encounter_counter)
        else:
            this_enemy = encounter
        if HD != None:
            HP = 0
            for x in range(0, HD):
                HP += randint(1, 8)
        encounter_set[this_enemy] = enemy_class(HP, AC, damage, morale)



    print encounter_set["monkey"].class_AC
    encounter_set["monkey"].class_AC -= 30
    print encounter_set["monkey"].class_AC
    exit()

class enemy_class(object):

    def __init__(self, class_HP, class_AC, class_damage, class_morale):
        self.class_HP = class_HP
        self.class_AC = class_AC
        self.class_damage = class_damage
        self.class_morale = class_morale





## Okay, so we need a class that maps everything, and a class that is an engine
## to run everything. The map will takes in an initial value, converts it to
## an entry in a dictionary. The engine takes that value, and runs it.


class map(object):

    processes = {
    "home": home(),
    "forest": forest(),
    "urban": urban(),
    "jungle": jungle(),
    "plains": plains(),
    "bathhouse": bathhouse(),
    "terrain_check": terrain_check(),
    "combat": combat(encounter, HD, AC, damage, morale, encounter_number)

    }

    def __init__(self, map_term):
        self.map_term = map_term

    def convert_next_process(self, map_entry):
        val = map.processes.get(map_entry)
        return val

    def find_next_process(self):
        #return map.processes[self.map_term]
        return self.convert_next_process(self.map_term)

# encounter, HD, AC, damage, morale, encounter_number = map("forest")
# print test.map_term

#next_step = map("home")

while True:
    next_step = next_step.map_term
    print next_step
    exit()
    if next_step.map_term in ['home', 'terrain_check']:
        next_step = map.find_next_process(next_step.map_term)
    elif next_step.map_term in ['forest', 'urban', 'jungle',
    'plains', 'bathhouse']:
        next_step, encounter, HD, AC, damage, morale, encounter_number = map.find_next_process(next_step)
    elif next_step.map_term == "combat":
        combat(encounter, HD, AC,
        damage, morale, encounter_number)
#home()
# test_2 = test.find_next_process(test.map_term)
# print test_2




#combat()
# while True:
#     next_step, encounter_number = forest()
#     while next_step != "home":
#         if next_step == "forest_end":
#             next_step = forest_end()
#         elif next_step == "combat":
#             combat()
