# create empty sets for columns 1 to 8
# read file
# for line in file, for x in range 0 to 7, add line[x] to appropriate column


#This is hella ugly goddamn. Figure out how to make this less ugly.


from sys import argv
import string

script, text = argv

column_one = []
column_two = []
column_three = []
column_four = []
column_five = []
column_six = []
column_seven = []
column_eight = []
count_one = 100
count_two = 100
count_three = 100
count_four = 100
count_five = 100
count_six = 100
count_seven = 100
count_eight = 100

alphabet = string.ascii_lowercase

with open(text) as f:
    for line in f:
        column_one.append(line[0])
        column_two.append(line[1])
        column_three.append(line[2])
        column_four.append(line[3])
        column_five.append(line[4])
        column_six.append(line[5])
        column_seven.append(line[6])
        column_eight.append(line[7])

for letter in alphabet:
    if column_one.count(letter) < count_one:
        count_one = column_one.count(letter)
        letter_one = letter
    if column_two.count(letter) < count_two:
        count_two = column_two.count(letter)
        letter_two = letter
    if column_three.count(letter) < count_three:
        count_three = column_three.count(letter)
        letter_three = letter
    if column_four.count(letter) < count_four:
        count_four = column_four.count(letter)
        letter_four = letter
    if column_five.count(letter) < count_five:
        count_five = column_five.count(letter)
        letter_five = letter
    if column_six.count(letter) < count_six:
        count_six = column_six.count(letter)
        letter_six = letter
    if column_seven.count(letter) < count_seven:
        count_seven = column_seven.count(letter)
        letter_seven = letter
    if column_eight.count(letter) < count_eight:
        count_eight = column_eight.count(letter)
        letter_eight = letter

answer = letter_one + letter_two + letter_three + letter_four + letter_five
answer = answer + letter_six + letter_seven + letter_eight

print answer
