#Make a class for each instruction, with a toggle var. Then when running follow instruction,
# it should jump to a different function for each function, after determining which instruction
# to follow, based on 1) the text of the instruction and 2) the toggle var.
import re
from sys import exit
import string

class Instruction(object):

    def __init__(self, rule, toggle=False):
        self.rule = rule
        self.toggle = toggle


instructions = []
registers = {"a": 0, "b": 0, "c": 0, "d": 0}
step = 0
instruction_length = 0


with open("aoc12.txt") as f:
    for line in f:
        check = re.match("cpy (.*?) (a|b|c|d)", line, re.I)
        if check:
            instructions.append(Instruction(check.group(0)))
            instruction_length += 1

        check = re.match("(inc|dec) (a|b|c|d)", line, re.I)
        if check:
            instructions.append(Instruction(check.group(0)))
            instruction_length += 1

        check = re.match("jnz (a|b|c|d|\d*) (\-*)(\d+)", line, re.I)
        if check:
            instructions.append(Instruction(check.group(0)))
            instruction_length += 1

        check = re.match("tgl (.)", line, re.I)
        if check:
            instructions.append(Instruction(check.group(0)))
            instruction_length += 1


def cpy(copy_from, copy_to):
    if copy_to not in registers:
        return 1

    elif copy_from in registers:
        registers[copy_to] = registers[copy_from]
        return 1

    else:
        registers[copy_to] = int(copy_from)
        return 1


def inc(val):
    registers[val] += 1
    return 1


def dec(val):
    registers[val] -= 1
    return 1

def jnz(check, jump):
    if (check in registers and registers[check] == 0) or check == '0':
        return 1

    else:
        return jump


def tgl(jump):
    if jump in registers:
        if registers[jump] not in range(0, instruction_length):
            return 1
        else:
            to_toggle = step + registers[jump]
            if instructions[to_toggle].toggle == False:
                instructions[to_toggle].toggle = True
            else:
                instructions[to_toggle].toggle = False
    elif jump in string.digits:
        to_toggle = step + int(jump)
        if to_toggle in range(0, instruction_length):
            if instructions[to_toggle].toggle == False:
                instructions[to_toggle].toggle == True
            else:
                instructions[to_toggle].toggle = False



def follow_instruction(line):
    instruction = re.match("cpy (.*?) (a|b|c|d)", line.rule, re.I)
    if instruction and line.toggle == False:
        # THIS IS WHAT WE WANT. THINGS LIKE THIS.
        return cpy(instruction.group(1), instruction.group(2))
    elif instruction and line.toggle == True:
        return jnz(instruction.group(1), instruction.group(2))


    if not instruction:
        instruction = re.match("(inc|dec) (a|b|c|d)", line.rule, re.I)
        if instruction:
            if (instruction.group(1) == "inc" and line.toggle == False) or (
                  instruction.group(2) == "dec" and line.toggle == True):
                return inc(instruction.group(2))
            else:
                return dec(instruction.group(2))


    if not instruction:
        instruction = re.match("jnz (a|b|c|d|\d*) (\-*)(\d+)", line.rule, re.I)
        if instruction:
            if instruction.group(2) == "-":
                second_val = 0 - int(instruction.group(3))
            else:
                second_val = int(instruction.group(3))

            if line.toggle == False:
                return jnz(instruction.group(1), second_val)
            elif line.toggle == True:
                return 1 #cpy(first_val, second_val)


    if not instruction:
        instruction = re.match("tgl (.)", line.rule, re.I)
        if instruction and line.toggle == False:
            return tgl(instruction.group(1))
        elif instruction and line.toggle == True:
            return inc(instruction.group(1))

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
