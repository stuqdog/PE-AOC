# First, we want to be able to read this multiple times, and edit it.
# So, let's read the document, and pop each line into a list as a string.
# Then, we can read the string, and as lines are followed, we delete them.
#
# So first we read through, give chips to the bots that start with them.
# Then, if a bot is called and it has two chips, we follow the orders.
#
# Each bot and output should start as an empty list within a broader dict
#
# with open file as f:
#   for line in f, instructions.append(line)
#
# for order in instructions:
#   if value in order
#     strip until we have the bot number and the value number
#     add bot number to dictionary as []
#     add value number to bot number
#     add order to remove_instruction
#
# for order in instructions:
#   if order in remove_instruction, delete the order from instructions
#
# then, for order in instructions
#   if the initial bot entry in dict has length[2], we distribute accordingly
#   after that, if bot entry contains 61 and 17, print that bot number and break

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


        for bot in bots:
            if sorted(bots[bot]) == [17, 61]:
                print bot
                exit()
