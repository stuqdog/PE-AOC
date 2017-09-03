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
    elif jump in string.digits:
        to_toggle = step + int(jump)
    if to_toggle in range(0, instruction_length):
        if instructions[to_toggle].toggle == True:
            return 1
        else:
            instructions[to_toggle].toggle = True
            if instructions[to_toggle].rule in ['dec', 'tgl']:
                instructions[to_toggle].rule = "inc"
            elif instructions[to_toggle].rule == 'inc':
                instructions[to_toggle].rule = 'dec'
            elif instructions[to_toggle].rule == "jnz":
                instructions[to_toggle].rule = "cpy"
            elif instructions[to_toggle].rule == 'cpy':
                instructions[to_toggle].rule = 'jnz'
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
    elif line.rule == "tgl":
            return tgl(line.var)
    else:
        print "There's a mistake"
        print step
        exit()


with open("aoc23.txt") as f:
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

        check = re.match("tgl (.)", line, re.I)
        if check:
            instructions.append(InstructionOne("tgl", check.group(1)))
            instruction_length += 1


while step < instruction_length:

    if (instructions[step].rule == 'inc' and instructions[step + 1].rule ==
          'dec' and instructions[step + 2].rule == "jnz"):
            if instructions[step + 2].var_two == -2:
                registers[instructions[step].var] += (
                  registers[instructions[step + 1].var])
                registers[instructions[step + 1].var] = 0
            if instructions[step + 3].rule == "dec" and (
                          instructions[step + 4].rule == "jnz" and
                          (instructions[step - 1].var_one) in registers):
                registers[instructions[step].var] += (
                        registers[instructions[step - 1].var_one]
                        * (registers[instructions[step + 3].var] - 1))
                registers[instructions[step + 3].var] = 0
                step += 4
            else:
                step += 2

    elif (instructions[step].rule == 'dec' and instructions[step + 1].rule ==
          'inc' and instructions[step + 2].rule == "jnz"):
            if instructions[step + 2].var_two == -2:
                registers[instructions[step + 1].var] += (
                  registers[instructions[step].var])
                registers[instructions[step].var] = 0
            if instructions[step + 3].rule == "dec" and (
                  instructions[step + 4].rule == "jnz" and
                  (instructions[step - 1].var_one) in registers):
                registers[instructions[step + 1].var] += (
                        registers[instructions[step - 1].var_one]
                        * (registers[instructions[step + 3].var] - 1))
                registers[instructions[step + 3].var] = 0
                step += 4
            else:
                step += 2

    else:
        step_change = follow_instruction(instructions[step])
        step += step_change

print registers
