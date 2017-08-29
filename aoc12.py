import re
from sys import exit

instructions = []
registers = {"a": 0, "b": 0, "c": 0, "d": 0}
step = 0
instruction_length = 0

def follow_instruction(line):
    instruction = re.match("cpy (.*?) (a|b|c|d)", line, re.I)
    if instruction:
        if instruction.group(1) in registers.keys():
            registers[instruction.group(2)] = int(
                                              registers[instruction.group(1)])
            return 1
        else:
            registers[instruction.group(2)] = int(instruction.group(1))
            return 1

    if not instruction:
        instruction = re.match("(inc|dec) (a|b|c|d)", line, re.I)
        if instruction:
            if instruction.group(1) == "inc":
                registers[instruction.group(2)] += 1
                return 1
            elif instruction.group(1) == "dec":
                registers[instruction.group(2)] -= 1
                return 1

    if not instruction:
        instruction = re.match("jnz (a|b|c|d|\d*) (\-*)(\d+)", line, re.I)

        if instruction.group(1) in registers.keys():
            if registers[instruction.group(1)] == 0:
                return 1
        elif instruction.group(1) == 0:
            return 1
        if instruction.group(2) == "-":
            step_mod = 0 - int(instruction.group(3))
        else:
            step_mod = int(instruction.group(3))
        return step_mod

    if not instruction:
        print "There's a mistake"
        print step
        exit()

with open("aoc12.txt") as f:
    for line in f:
        instructions.append(line)
        instruction_length += 1

while step < instruction_length:

    step_change = follow_instruction(instructions[step])
    step += step_change


print registers
