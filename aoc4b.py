#1 separate out the number as Cycle_Num. Separate out code as Code.
#2 create cypher, string.ascii_lowercare * 2.
#3 Cycle = Cycle_Num % 26
#4 for x in code:
#5  for y in cypher:
#6    if x == y:
#7      translation += cypher(y + cycle)
#8      break
#9  print translation


from sys import argv
import string

script, text = argv

letters = string.ascii_lowercase
numbers = string.digits

# *2 so we can cycle forward back to the start (from x to c, e.g.)
cypher = letters * 2

# by stripping this from a line, we are left with just the sector ID
cycle_num_reduce = "%s[]-\n" % letters

# by rstripping this from a line, we are left with just the code
code_reduce = "%s[]\n%s" % (letters, numbers)

# This reads lines, converts them forward in the cypher, and saves the result.
with open(text) as f:
    for line in f:
        solution = " "
        cycle_num = int(line.strip(cycle_num_reduce))
        # no need to cycle more than 26 times.
        cycle = cycle_num % 26
        code = line.rstrip(code_reduce)
        for x in code:
            for y in range(0, 26):
                if x == cypher[y]:
                    solution_add = cypher[y + cycle]
                    solution += solution_add
                    break
            if x == "-":
                solution += " "
        if "north" in solution:
            print solution
            print cycle_num
