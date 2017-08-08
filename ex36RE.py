## Currently, Forest is the only function that's set up with a decent regex.
## So, copy that for the other 4.

## If values might not always appear in an entry (like "HD: 4") but you always
## want to search for it, then create a regex expression like so: "(HD: %d)?"
## The ? ensures that we find what we're looking for even if the entry
## doesn't occur

from random import randint
import re


def forest():
    with open('forest.txt') as f:
        i = len(f.readlines())

    roll = randint(1, i)

    with open('forest.txt') as f:
        for x in range(1, roll + 1):
            result = f.readline().strip("\n")

## Regex to pull out relevant stats, which get put into dict combat_stats
    test = '(\d*)d(\d*) (.*) <(H[D|P]): (\d*), AC: (\d*),'
    test += ' damage: (\d*)d(\d*), morale: (\d*)>,'
    entry = re.match(test, result, re.I)

    entry_stats = re.search("( <.*>)", result, re.I)
    stat_dump = entry_stats.group(1)


    if entry:
        die_num = int(entry.group(1))
        die_size = int(entry.group(2))
        encounter = entry.group(3)
        if entry.group(4) == "HP":
            HP = int(entry.group(5))
            HD = 0
        elif entry.group(4) == "HD":
            HD = int(entry.group(5))
            HP = 0

        AC = entry.group(6)
        damage = [int(entry.group(7)), int(entry.group(8))]
        morale = entry.group(9)


    else:
        print "ERROR. Please confirm proper formatting of encounter entry."
        return "home", {}


    encounter_number = 0
    for r in range(0, int(die_num)):
        encounter_number += randint(1, int(die_size))

    if encounter_number > 1:
        print encounter_number, re.sub(stat_dump, '',
                                      (result.lstrip("1234567890d")).lstrip())
    else:
        print re.sub(stat_dump, '',
                    (result.lstrip("1234567890d")).lstrip())
    combat_stats = {
        'stat_dump': stat_dump,
        'encounter_number': encounter_number,
        'encounter': encounter,
        'HP': HP,
        'HD': HD,
        'AC': AC,
        'damage': damage,
        'morale': morale
    }

    while True:
        next_step = raw_input("> ")
        if next_step == "ct":
            return "terrain_check", combat_stats
        elif next_step == "combat":
            return "combat", combat_stats
        elif next_step == "home":
            return "home", combat_stats
        elif next_step == "stats":
            print stat_dump
        elif next_step == "exit":
            exit(0)
        elif next_step == "help":
            print""" ct: Change terrain
     combat: combat
     home: return home
     exit: quit program
     anything else: generate new forest encounter"""
        else:
            return "forest", combat_stats


def urban():
    pass

def miscellaneous():
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

    combat_stats = {
        "encounter_number": encounter_number,
        "encounter": encounter
    }

    while True:

        next_step = raw_input("> ")
        if next_step == "ct":
            return "terrain_check", combat_stats
        elif next_step == "combat":
            return "combat", combat_stats
        elif next_step == "home":
            return "home", combat_stats
        elif next_step == "exit":
            exit(0)
        elif next_step == "help":
            print""" ct: Change terrain
     combat: combat
     home: return home
     exit: quit program
     anything else: generate new urban encounter"""
        else:
            return "misc", combat_stats

def jungle():
    return "home", "blah"
    pass

def plains():
    pass
