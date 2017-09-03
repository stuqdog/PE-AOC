import re
from sys import exit
import string

instructions = []
registers = {"a": 7, "b": 0, "c": 0, "d": 0}
step = 0
instruction_length = 0

class InstructionOne(object):

    def __init__(self, rule, var, toggle=False):
        self.rule = rule
        self.var = var
        self.toggle = toggle

class InstructionTwo(object):

    def __init__(self, rule, var_one, var_two, toggle=False):
        self.rule = rule
        self.var_one = var_one
        self.var_two = var_two
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
            return jump

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

# This just tells us to follow instructions
def follow_instruction(line):

    if line.rule == "cpy":
        if line.toggle == False:
            return cpy (line.var_one, line.var_two)
        else:
            return jnz(line.var_one, line.var_two)

    elif line.rule == "inc":
        if line.toggle == False:
            return inc(line.var)
        else:
            return dec(line.var)

    elif line.rule == "dec":
        if line.toggle == False:
            return dec(line.var)
        else:
            return inc(line.var)

    elif line.rule == "jnz":
        if line.toggle == False:
            return jnz(line.var_one, line.var_two)
        else:
            return cpy(line.var_one, line.var_two)

    elif line.rule == "tgl":
        if line.toggle == False:
            return tgl(line.var)
        else:
            return inc(line.var)

    else:
        print "There's a mistake"
        print step
        exit()

#This just gets us our instructions.
with open("aoc23.txt") as f:
    for line in f:
        sucess = False
        check = re.match("cpy (.*?) (a|b|c|d)", line, re.I)
        if check:
            instructions.append(InstructionTwo("cpy", check.group(1),
                                            check.group(2)))
            instruction_length += 1
            sucess = True

        check = re.match("(inc|dec) (a|b|c|d)", line, re.I)
        if check:
            instructions.append(InstructionOne(check.group(1), check.group(2)))
            instruction_length += 1
            sucess = True

        check = re.match("jnz (a|b|c|d|\d*) (\-*)(.+)", line, re.I)
        if check:
            if check.group(2) == "-":
                second_var = 0 - int(check.group(3))
            elif check.group(3) in string.digits:
                second_var = int(check.group(3))
            else:
                second_var = check.group(3)
            instructions.append(InstructionTwo("jnz", check.group(1),
                                               second_var))
            instruction_length += 1
            sucess = True

        check = re.match("tgl (.)", line, re.I)
        if check:
            instructions.append(InstructionOne("tgl", check.group(1)))
            instruction_length += 1
            sucess = True

        if sucess == False:
            print "ERROR HERE"
            print line


while step < instruction_length:

    step_change = follow_instruction(instructions[step])
    step += step_change

print registers
