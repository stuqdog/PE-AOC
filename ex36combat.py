def combat():
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



    while self.encounter_total != {}:

        for enemy in self.encounter_print:
            print "%d. %s (%d/%d)" % (enemy_number,
                enemy.rstrip("1234567890s "),
                self.encounter_total[enemy].HP
                - self.encounter_total[enemy].damage_taken,
                self.encounter_total[enemy].HP)
            enemy_number += 1

        if side == 'PC':
            print "---\n"
            enemy_number = 1
            option = raw_input("> ")

            if option == "change side" or option == "cs":
                side = "NPC"

            elif option == "exit":
                exit()

            elif option == "list" or option == "list enemies":
                enemy_number = 1
                for enemy in self.encounter_print:
                    print "%d. %s" % (enemy_number, enemy)
                    enemy_number += 1

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
