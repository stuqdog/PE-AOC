# random encounter program
# write initial section: giving options about terrain, etc
# write terrain-specific sections, give option to change from night to day, etc.
# build in option to move directly from somewhere to home, or to forest,
# or to plains, etc.

#TO DO:

    # Use classes and regex to create a clean combat option.
    # Convert scenes to classes.

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


    # Currently, the Engine play is too simple, doesn't account for
    # potentially needing to return different vars/different number of vars.
        # this should be solved by putting stats into a dictionary.
    # PUT COMBAT STATS FOR GENERATING ENEMIES INTO A DICTIONARY!!!


## Variables used:
## encounter_set = dictionary of enemies in current combat encounter



from random import randint
import string
import re
import ex36RE
from sys import exit

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
            # Is this necessary? Can we put this in our dict in the map class
            # instead, make it combat(encounter_stats) instead of combat()?
            if current_feature == "combat":
                current_feature, combat_stats = Combat(combat_stats).enter()
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



class Terrain_Check(Feature):

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



class Encounter_Class(object):

    def __init__(self, HD, HP, AC, damage, morale):
        self.HD = HD
        self.HP = HP
        self.AC = AC
        self.damage = damage
        self.morale = morale

    def take_damage(self, damage_taken):
        self.HP -= damage_taken


class Combat(Feature):

    ## THIS IS HELLA CLUNKY AND GETTING GROSS. Figure out how to use the
    ## encounter_class class to make it easier. Might be good to make use of
    ## super in there?

    def __init__(self, combat_stats):
        self.encounter_total = {}
        self.encounter_name = self.combat_stats[encounter_name]
        if self.combat_stats[encounter_number] == 1:
            self.encounter_total[self.]
        for i in range(0, combat_stats[encounter_number]):
            self.encounter_total.append()

        self.combat_stats = combat_stats

    def enter(self):
        print "we made it! :D"
        print self.combat_stats
        exit()

    # We need to, when going to combat from an encounter, return the result from
    # that encounter. make that the template for combat, but let us replace it
    # if we want. Then use classes to turn it into enemies, and put those class
    # occurrences in a dictionary. class features are HP, damage, AC, to hit,
    # maybe spells, for casters, maybe a way to capture unique abilities?
    # then we have combat simulation for those things, when their HP is reduced
    # to zero, we delete them from our combat dictionary. Learn regex to cleanly
    # reduce encounter results into numbers and strings for the actual encounter
        pass
    # encounter_number, encounter, HD, HP, AC, damage, morale
    # encounter_set = {} ## this line should be moved down, so we can add new enemies mid-fight.
    # for i in range(0, encounter_number):
    #     add_enemy = encounter.rstrip("s") + " %s" % str(i + 1)
    #     print add_enemy
    #     if HP == 0:
    #         enemy_specific_HP = 0
    #         for x in range(0, HD):
    #             enemy_specific_HP += randint(1, 8)
    #     else:
    #         enemy_specific_HP = HP
    #     encounter_set[add_enemy] = Encounter_Class(HD, enemy_specific_HP,
    #     AC, damage, morale)
    #
    # for enemy in encounter_set:
    #     print encounter_set[enemy].HP
    #
    # ## This makes sure combat continues as long as we have enemies left over.
    # while encounter_set != {}:
    #     pass
    #     ## Make sure we do some combat stuff
    #
    # exit()



class Map(object):

    features = {
    "urban": Urban(),
    "forest": Forest(),
    "plains": Plains(),
    "jungle": Jungle(),
    "misc": Miscellaneous(),
    "combat": Combat({}),
    "home": Home(),
    "terrain_check": Terrain_Check()
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
