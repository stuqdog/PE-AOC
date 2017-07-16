# Less ugly solution


from sys import argv
import string

script, text = argv

solution = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
letter_total = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

alphabet = string.ascii_lowercase

with open(text) as f:
    for line in f:
        for x in range(0, 8):
            letter_total[x] += line[x]


for x in range(0, 8):
    count = 100
    for letter in alphabet:
        if letter_total[x].count(letter) < count:
            count = letter_total[x].count(letter)
            solution[x] = letter

print solution
