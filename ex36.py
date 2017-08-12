# TO DO:

    # 1. Use classes and regex to create a clean combat option.
    # 2. Make it so we can add new enemies in combat. If we want to do that, we
    #    can return an encounter and then, for entry in returned_encounter,
    #    our_encounter[entry] = returned_encounter[entry]
    # 3. Create the option to manually enter combat stats, rather than
    #    using only what we have been provided by the random encounter table.
    # 4. Find out if we need to return combat_stats from combat in the Engine.
    # 5. Create settings to have NPCs attack the PCs.
    # 6. Get comfortable with exceptions and stuff, so we can have the program
    #    remind the user to enter a proper value if they enter text where an
    #    int is called for.
    # 7. Randomize weapons! Give enemies the option to use different weapons
    #    and import weapon stuff from Courtney's thing.
    #       If you want to go all-out, can limit types of weapons a class or
    #       encounter can possibly use.
    # 8. This might be cleaner if we offload some of the combat methods into
    #    a new file that we can import (call it ex36combat.py).

#************
    # Combat should work differently from other features, because it has to
    # take in the encounter stats. Can we put that in our map class, or do we
    # need an exception on the engine class? Should experiment with this to
    # find out.

    # Looks like the answer is no, since the combat_stats variable won't be
    # defined within the map. So, we make an exception in the engine. This is
    # good go know, because it means with enough exceptions, it's probably best
    # to just put the mapping into the Engine class. Alternatively, could we
    # stick the combat_stats var into the Map somehow? Hmm. Probably not, since
    # it's not defined yet. Unless it was in an __init__?? That seems kinda
    # complicated though, probably best to hold off on figuring that out until
    # you have to.
#************


## Variables used:
##   encounter_total = dictionary of enemies in current combat encounter



from random import randint
from sys import exit
import string
import re
import ex36RE
import ex36combat

class Feature(object):

    def enter(self):
        print """This feature is not implemented yet. Please implement
 with an enter function."""
        print "----------\n"
        return "home", {}


class Engine(object):

    combat_stats = {}

    def __init__(self, feature_map):
        self.feature_map = feature_map

    def play(self):
        next_feature_name = self.feature_map.starting_feature()
        current_feature = "home"

        while True:
            # Do we need to return combat_stats from combat? probably not.
            if current_feature == "combat":
                current_feature = Combat(combat_stats).enter()
            else:
                current_feature, combat_stats = next_feature_name.enter()
            next_feature_name = self.feature_map.next_feature(current_feature)



class Home(Feature):

    def enter(self):

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
            return "terrain_check", {}
        elif answer == "2":
            return "combat", {}



class TerrainCheck(Feature):

    def enter(self):

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
            return "urban", {}
        elif answer_t == "2":
            return "forest", {}
        elif answer_t == "3":
            return "jungle", {}
        elif answer_t == "4":
            return "plains", {}
        elif answer_t == "5":
            return "misc", {}


class Urban(Feature):

    pass
    # This is good
    # -----
    # def enter(self):
    #     return ex36RE.urban()
    # -----
    #this is good


class Miscellaneous(Feature):

    def enter(self):
        return ex36RE.miscellaneous()



class Forest(Feature):

    def enter(self):
        return ex36RE.forest()



class Jungle(Feature):
    pass
    # print "Jungle TK"


class Plains(Feature):
    pass
    # print "Plains TK"



class CombatEnemy(object):

    def __init__(self, combat_stats):
        self.damage_taken = 0
        self.HD = combat_stats['HD']
        self.HP = combat_stats['HP']
        self.encounter_name = combat_stats['encounter_name'].rstrip('s')
        # print self.HP
        if self.HP == 0:
            for i in range(0, self.HD):
                self.HP += randint(1, 12)
        self.AC = combat_stats['AC']
        self.damage = combat_stats['damage']
        self.morale = combat_stats['morale']
        self.morale_pass = True
        self.morale_check_number = 0

    def attacked(self, to_hit_roll):
## This implements attacks against the encounter_total group.
        attack_hit = False
        crit_hit = 1

        if to_hit_roll == 1:
            print "CRITICAL FAILURE"
            print "What happens now? Details TK"
            return False
        elif to_hit_roll == 20:
            print "CRITICAL HIT!!"
            print "Double damage, this needs to be implemented."
            attack_hit, crit_hit = True, 2
        elif to_hit_roll >= self.AC:
            print "You hit!"
            attack_hit = True

        if attack_hit == True:
            damage_suffered = raw_input("Damage?\n> ")
            damage_check = re.match("(\d*)d?(\d*)?( )?(\+|\-)?( )?(\d*)?",
                                    damage_suffered, re.I)
            if damage_check.group(2):
                for i in range(0, crit_hit * int(damage_check.group(1))):
                    self.damage_taken += randint(1, int(damage_check.group(2)))
                if damage_check.group(4) == "+":
                    self.damage_taken += crit_hit * int(damage_check.group(6))
                elif damage_check.group(4) == "-":
                    self.damage_taken -= crit_hit * int(damage_check.group(6))
            else:
                self.damage_taken += crit_hit * int(damage_suffered)
        else:
            print "YOU MISSED!"

## This is returning an enemy_defeated value. We can remove enemies from the
## encounter as they are defeated.

        if self.damage_taken > self.HP:
            return True
        else:
            return False

    def attacking(self):
        # This is how we'll attack the party.
        pass

    def morale_check(self):
        # this is for checking morale.



class Combat(Feature):

    ## THIS IS HELLA CLUNKY AND GETTING GROSS. Figure out how to use the
    ## encounter_class class to make it easier. Might be good to make use of
    ## super in there?
    ## We are moving into multiple inheritance here sorta, with Combat being a
    ## Feature and Combat_Enemy being a Combat.
    ## Possibly, might want to make Combat_Enemy an object, and just use the
    ## instances it creates within Combat without inheriting.

    def __init__(self, combat_stats):
        self.combat_stats = combat_stats
        self.encounter_total = {}
        self.encounter_print = []
        self.encounter_name = combat_stats['encounter_name']
        self.encounter_number = combat_stats['encounter_number']
        if combat_stats['encounter_number'] == 1:
            self.encounter_total[self.encounter_name] = (
                CombatEnemy(combat_stats))
            self.encounter_print.append(self.encounter_name)
        else:
            for i in range(1, combat_stats['encounter_number'] + 1):
                this_enemy = (combat_stats['encounter_name']
                              + " %s" % str(i))
                self.encounter_total[this_enemy] = CombatEnemy(combat_stats)
                self.encounter_print.append(this_enemy)



    def enter(self):
        enemy_number = 1
        print"""\n------

It's combat time! Whose turn is it?
 1. The PCs
 2. The NPCs"""

        determine_side = raw_input("> ")
        while True:
            if determine_side in ['1', '2']:
                break
            else:
                print "Please select 1 or 2."

        if determine_side == '1':
            side = 'PC'
        else:
            side = 'NPC'


        while self.encounter_total != {}

            for enemy in self.encounter_print:
                print "%d. %s (%d/%d)" % (enemy_number,
                    enemy.rstrip("1234567890s "),
                    self.encounter_total[enemy].HP
                    - self.encounter_total[enemy].damage_taken,
                    self.encounter_total[enemy].HP)
                enemy_number += 1
            encounter_remaining = enemy_number

        # this triggers morale check as long as we haven't done two already.
        # HUH. This is gonna be tough. We can't just return that an enemy has
        # failed a morale check, because then we leave. We'll have to set a
        # self.morale_check variable, and change it to false for an encounter
        # if that encounter failed morale. Then, if it's false, the encounter
        # bails. Should also consider where the best place to position this
        # check is. The actual code to do the morale check will go in the
        # CombatEnemy class.
            if (encounter_remaining < self.encounter_number / 2 and
                  morale_check < 2):
                for enemy in self.encounter_total:
                    enemy.morale_check

            if side == 'PC':
                print "---\n"
                enemy_number = 1
                option = raw_input("> ")

                if option == "change side" or option == "cs":
                    side = "NPC"

                elif option == "exit":
                    exit()

                elif option == "list" or option == "list enemies":
                    for enemy in self.encounter_print:
                        print "%d. %s" % (enemy_number, enemy)
                        enemy_number += 1
                    enemy_number = 1

                elif option == "home":
                    return "home"

                elif "attack" in option:
                    # groups 1 and 3 are fluff, groups 2 and 4 are the target
                    # and the to-hit mod
                    attack_order = re.search("attack(.?)(\d*)?(, )?(\d*)?",
                                                  option, re.I)
                    if attack_order.group(2):
                        target = int(attack_order.group(2)) - 1
                    else:
                        target = int(raw_input("Which target?\n> ")) - 1
                    if attack_order.group(4):
                        attack_mod = int(attack_order.group(4))
                    else:
                        attack_mod = int(raw_input("Attack mod?\n> "))
                    to_hit_roll = randint(1, 20)
                    if to_hit_roll not in [1, 20]:
                        to_hit_roll += attack_mod

                    # this checks to see if we've killed the enemy, and removes
                    # them from the dict if we have.
                    enemy_defeated = self.encounter_total[
                        self.encounter_print[target]].attacked(to_hit_roll)
                    if enemy_defeated == True:
                        print "ENEMY DEAD"
                        del self.encounter_total[self.encounter_print[target]]
                        del self.encounter_print[target]
                        exit()

            elif side == "NPC":
                print "THIS IS NOT YET IMPLEMENTED."
                pass
                ## NEED TO FILL THIS IN






class Map(object):

    starting_combat_stats = {'morale': 0, 'encounter_name': 'ERROR',
     'stat_dump': ' <HD: 6, AC: 12, damage: 1d12, Morale: 8>',
     'encounter_number': 4, 'HP': 0, 'AC': '12', 'HD': 6, 'damage': [1, 12]}

    features = {
    "urban": Urban(),
    "forest": Forest(),
    "plains": Plains(),
    "jungle": Jungle(),
    "misc": Miscellaneous(),
    "combat": Combat(starting_combat_stats),
    "home": Home(),
    "terrain_check": TerrainCheck()
    }

    def __init__(self, initial_feature):
        self.initial_feature = initial_feature


    def next_feature(self, feature_name):
        val = Map.features.get(feature_name)
        return val

    def starting_feature(self):
        return self.next_feature(self.initial_feature)


party_time = Map("home")
rad_party = Engine(party_time)
rad_party.play()
