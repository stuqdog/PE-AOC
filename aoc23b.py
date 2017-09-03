# How about this: instead of regexing constantly, let's just do it once and then
# set the variables. So we'll need two classes: InstructionOne and InstructionTwo.
# Then, we can say "oh, if this says add one and the next one says subtract one
# and the third says go back 2, we can just say first += 2nd, second = 1, go."


import re
from sys import exit
import string

instructions = []
registers = {"a": 12, "b": 0, "c": 0, "d": 0}
step = 0
instruction_length = 0

class Instruction(object):

    def __init__(self, rule, toggle=False):
        self.rule = rule
        self.toggle = toggle


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
    if (check in registers and registers[check] == 0) or check in [0, '0']:
        return 1
    else:
        if jump in registers:
            return registers[jump]
        else:
            return int(jump)

def tgl(jump):
    if jump in registers:
        print registers[jump] + step
        to_toggle = step + registers[jump]
        if to_toggle in range(0, instruction_length):
            if instructions[to_toggle].toggle == False:
                instructions[to_toggle].toggle = True
        return 1
    elif jump in string.digits:
        to_toggle = step + int(jump)
        if to_toggle in range(0, instruction_length):
            if instructions[to_toggle].toggle == False:
                instructions[to_toggle].toggle == True
        return 1


def follow_instruction(line):
    instruction = re.match("cpy (.*?) (a|b|c|d)", line.rule, re.I)
    if instruction and line.toggle == False:
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
        instruction = re.match("jnz (a|b|c|d|\d*) (\-*)(.+)", line.rule, re.I)
        if instruction:
            if instruction.group(2) == "-" and (
                       instruction.group(3) in string.digits):
                second_val = 0 - int(instruction.group(3))
            elif instruction.group(3) in string.digits:
                second_val = int(instruction.group(3))
            else:
                second_val = instruction.group(3)

            if line.toggle == False:
                return jnz(instruction.group(1), second_val)
            elif line.toggle == True:
                return cpy(instruction.group(1), second_val)

    if not instruction:
        instruction = re.match("tgl (.*)", line.rule, re.I)
        if instruction and line.toggle == False:
            return tgl(instruction.group(1))
        elif instruction and line.toggle == True:
            return inc(instruction.group(1))

    if not instruction:
        print "There's a mistake"
        print step
        exit()


with open("aoc23.txt") as f:
    for line in f:
        sucess = False
        check = re.match("cpy (.*?) (a|b|c|d)", line, re.I)
        if check:
            instructions.append(Instruction(check.group(0)))
            instruction_length += 1
            sucess = True

        check = re.match("(inc|dec) (a|b|c|d)", line, re.I)
        if check:
            instructions.append(Instruction(check.group(0)))
            instruction_length += 1
            sucess = True

        check = re.match("jnz (a|b|c|d|\d*) (\-*)(.+)", line, re.I)
        if check:
            instructions.append(Instruction(check.group(0)))
            instruction_length += 1
            sucess = True

        check = re.match("tgl (.)", line, re.I)
        if check:
            instructions.append(Instruction(check.group(0)))
            instruction_length += 1
            sucess = True

        if sucess == False:
            print "ERROR HERE"
            print line

print instruction_length
while step < instruction_length:
    print registers

    step_change = follow_instruction(instructions[step])
    step += step_change

print registers
