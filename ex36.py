# random encounter program
# write initial section: giving options about terrain, etc
# write terrain-specific sections, give option to change from night to day, etc.
# build in option to move directly from somewhere to home, or to forest,
# or to plains, etc.

#TO DO: Convert this into classes. We can make a terrain class, a combat class,
#etc. etc. Could be cleaned up nicely.

    # Use classes and regex to create a clean combat option.


## Variables used:
## encounter_set = dictionary of enemies in current combat encounter


from random import randint
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
    elif answer_t == "2":
        return "forest"
    elif answer_t == "3":
        return "jungle"
    elif answer_t == "4":
        return "plains"
    elif answer_t == "5":
        return "bathhouse"


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
        return "terrain_check"
    elif next_step == "combat":
        return "combat",
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
            return "terrain_check"
        elif next_step == "combat":
            return "combat", encounter_number, encounter, HD, HP, AC, damage, morale
        elif next_step == "home":
            return "home"
        elif next_step == "exit":
            exit(0)
        elif next_step == "help":
            print""" ct: Change terrain
     combat: combat
     home: return home
     exit: quit program
     anything else: generate new urban encounter"""
        else:
            return "forest", None, None, None, None, None, None, None









def jungle():
    print "Jungle TK"
def plains():
    print "Plains TK"



class Encounter_Class(object):

    def __init__(self, HD, HP, AC, damage, morale):
        self.HD = HD
        self.HP = HP
        self.AC = AC
        self.damage = damage
        self.morale = morale


def combat(encounter_number, encounter, HD, HP, AC, damage, morale):

    # We need to, when going to combat from an encounter, return the result from
    # that encounter. make that the template for combat, but let us replace it
    # if we want. Then use classes to turn it into enemies, and put those class
    # occurrences in a dictionary. class features are HP, damage, AC, to hit,
    # maybe spells, for casters, maybe a way to capture unique abilities?
    # then we have combat simulation for those things, when their HP is reduced
    # to zero, we delete them from our combat dictionary. Learn regex to cleanly
    # reduce encounter results into numbers and strings for the actual encounter

    encounter_set = {} ## this line should be moved down, so we can add new enemies mid-fight.
    for i in range(0, encounter_number):
        enemy_number = i + 1
        enemy_number = str(enemy_number)
        add_enemy = encounter.rstrip("s") + " " + enemy_number #%s" % str(i + 1)
        print add_enemy
        if HP == None:
            specific_HP = 0
            for x in range(0, HD):
                specific_HP += randint(1, 8)
        else:
            specific_HP = HP
        encounter_set[add_enemy] = Encounter_Class(HD, specific_HP, AC, damage, morale)

    for enemy in encounter_set:
        print encounter_set[enemy].HP

    exit()




next_step = home()

while True:
    if next_step == "terrain_check":
        next_step = terrain_check()

    elif next_step == "home":
        next_step = home()

    elif next_step == "forest":
        next_step, encounter_number, encounter, HD, HP, AC, damage, morale = forest()

    elif next_step == "urban":
        next_step, encounter_number, encounter, HD, HP, AC, damage, morale = urban()

    elif next_step == "jungle":
        next_step, encounter_number, encounter, HD, HP, AC, damage, morale = jungle()

    elif next_step == "plains":
        next_step, encounter_number, encounter, HD, HP, AC, damage, morale = plains()

    elif next_step == "bathhouse":
        next_step, encounter_number, encounter, HD, HP, AC, damage, morale = bathhouse()

    elif next_step == "combat":
        next_step = combat(encounter_number, encounter, HD, HP, AC, damage, morale)
