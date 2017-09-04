import re
from sys import exit
import string

instructions = []
start_value = 0
registers = {"a": 0, "b": 0, "c": 0, "d": 0}
step = 0
instruction_length = 0
output = []

class InstructionOne(object):

    def __init__(self, rule, var):
        self.rule = rule
        self.var = var

class InstructionTwo(object):

    def __init__(self, rule, var_one, var_two):
        self.rule = rule
        self.var_one = var_one
        self.var_two = var_two


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

def out(val):
    output.append(registers[val])
    return 1


def follow_instruction(line):

    if line.rule == "cpy":
        return cpy(line.var_one, line.var_two)
    elif line.rule == "inc":
        return inc(line.var)
    elif line.rule == "dec":
        return dec(line.var)
    elif line.rule == "jnz":
        return jnz(line.var_one, line.var_two)
    elif line.rule == "out":
        return out(line.var)
    else:
        print "There's a mistake"
        print step
        exit()


with open("aoc25.txt") as f:
    for line in f:
        check = re.match("cpy (.*?) (a|b|c|d)", line, re.I)
        if check:
            instructions.append(InstructionTwo("cpy", check.group(1),
                                            check.group(2)))
            instruction_length += 1

        check = re.match("(inc|dec) (a|b|c|d)", line, re.I)
        if check:
            instructions.append(InstructionOne(check.group(1), check.group(2)))
            instruction_length += 1

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

        check = re.match("out (a|b|c|d)", line, re.I)
        if check:
            instructions.append(InstructionOne("out", check.group(1)))
            instruction_length += 1


while True:

    step_change = follow_instruction(instructions[step])
    step += step_change

    for value in output:
        if value not in [0, 1]:
            step = 0
            start_value += 1
            registers = {'a': start_value, 'b': 0, 'c': 0, 'd': 0}
            output = []
            break

    if len(output) > 1 and output[-1] == output[-2]:
        step = 0
        start_value += 1
        registers = {'a': start_value, 'b': 0, 'c': 0, 'd': 0}
        output = []

    if len(output) >= 10:
        break

print start_value
