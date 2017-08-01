from sys import exit
import re

instructions = []
bots = {}
delete_orders = []
delete_entry = 0
import string

with open("aoc10.txt") as f:
    for line in f:
        entry = line.rstrip("\n")
        instructions.append(entry)

for order in instructions:
    if "value" in order:
        num_and_val = re.search(r'value (\d*) goes to (.*)', order)
        bot_number = num_and_val.group(2)
        value = int(num_and_val.group(1))

        if bot_number in bots:
            bots[bot_number].append(value)
        else:
            bots[bot_number] = [value]
        delete_orders.append(delete_entry)
    delete_entry += 1

for entry in reversed(delete_orders):
    del instructions[entry]


while True:
    delete_orders = []
    delete_entry = 0

    for order in instructions:
        bot_values = re.search(r'(.*?) gives low to (.*?) and high to (.*)', order)
        bot_number = bot_values.group(1)
        low_bot = bot_values.group(2)
        high_bot = bot_values.group(3)

        if bot_number not in bots:
            bots[bot_number] = []
        if low_bot not in bots:
            bots[low_bot] = []
        if high_bot not in bots:
            bots[high_bot] = []

        if len(bots[bot_number]) == 2:
            bots[bot_number] = sorted(bots[bot_number])
            bots[high_bot].append(bots[bot_number][1])
            bots[low_bot].append(bots[bot_number][0])
            bots[bot_number] = []

        if "output 0" in bots and "output 1" in bots and "output 2" in bots:
            if (bots["output 0"] != [] and bots["output 1"] != [] and
            bots["output 2"] != []):
                print (bots["output 0"][0] * bots["output 1"][0]
                * bots["output 2"][0])
                exit()
