from sys import exit

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
        reduced_order = order.strip("value \n")
        bot_number = reduced_order.lstrip(string.digits)
        bot_number = bot_number.lstrip("goes to ")
        value = reduced_order.rstrip(string.digits)
        value = int(value.strip("value goes to bot \n"))
        if bot_number in bots:
            bots[bot_number].append(value)
        else:
            bots[bot_number] = [value]
        delete_orders.append(delete_entry)
    delete_entry += 1

for entry in reversed(delete_orders):
    del instructions[entry]

#print instructions

while True:
    delete_orders = []
    delete_entry = 0
    for order in instructions:
    # this is atrocious and should be regex. learn. fix it.
        bot_and_low = order.rstrip(string.digits)
        bot_and_low = bot_and_low.rstrip("and high to bot output")
        bot_number = bot_and_low.rstrip(string.digits)
        bot_number = bot_number.rstrip("gives low to bot output")
        low_bot = bot_and_low.lstrip("bot ")
        low_bot = low_bot.lstrip(string.digits)
        low_bot = low_bot.lstrip("gives low")
        low_bot = low_bot.lstrip("to")
        low_bot = low_bot.strip()
        high_bot = order.lstrip("bot ")
        high_bot = high_bot.lstrip(string.digits)
        high_bot = high_bot.lstrip("gives low to bot output")
        high_bot = high_bot.lstrip(string.digits)
        high_bot = high_bot.lstrip("and high")
        high_bot = high_bot.lstrip("to")
        high_bot = high_bot.strip()

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
