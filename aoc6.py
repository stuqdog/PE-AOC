# create empty sets for columns 1 to 8
# read file
# for line in file, for x in range 0 to 7, add line[x] to appropriate column


#This is hella ugly goddamn. Figure out how to make this less ugly.


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
    count = 0
    for letter in alphabet:
        if letter_total[x].count(letter) > count:
            count = letter_total[x].count(letter)
            solution[x] = letter

print solution
