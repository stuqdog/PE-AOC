import re

with open('aoc7.txt') as f:
    instructions = [line.strip() for line in f]

def bad_abba_check(line):
    check = line.replace(']', '[').split('[')
    for x in range(1, len(check), 2):
        a = re.search(r'(.)(.)\2\1', check[x])
        if a and a[1] != a[2]:
            return False
    return True

def good_abba_check(line):
    check = line.replace(']', '[').split('[')
    for x in range(0, len(check), 2):
        a = re.search(r'(.)(.)\2\1', check[x])
        if a and a[1] != a[2]:
            return True
    return False

def aba_check(line):
    check = line.replace(']', '[').split('[')
    a = []
    for x in range(0, len(check), 2):
        for i in range(2, len(check[x])):
            if check[x][i] == check[x][i-2] != check[x][i-1]:
                a.append((check[x][i], check[x][i-1]))
    return a

def bab_check(abas, line):
    check = line.replace('[', ']').split(']')
    for x in range(1, len(check), 2):
        for aba in abas:
            bab = aba[1] + aba[0] + aba[1]
            if bab in check[x] and bab[0] != bab[1]:
                return True
    return False


print(sum(1 for line in instructions if bad_abba_check(line) and good_abba_check(line)))
print(sum(1 for line in instructions if bab_check(aba_check(line), line)))
