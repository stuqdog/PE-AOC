from sys import argv
import string

letters = string.ascii_letters
numbers = string.digits
first_strip = "%s[]\n" % letters
all_but_numbers = "%s[]-\n" % letters

solution = 0

script, text = argv

with open(text) as f:
    for line in f:
        match = True

        # tracking the five most common letters
        char_one, char_two, char_three, = None, None, None
        char_four, char_five = None, None

        # tracking the # of occurrences of char_one through char_five
        char_one_num, char_two_num, char_three_num = 0, 0, 0
        char_four_num, char_five_num = 0, 0

        # strips \n from lines so we have a consistent placement of the 5 letter
        # key's placement relative to the end of the line
        line_s = line.rstrip("\n")

        # creates our key
        key = [line_s[-6], line_s[-5], line_s[-4], line_s[-3], line_s[-2]]

        #removes key from the line so it doesn't get counted in our test.
        sort_line = line.rstrip(first_strip)

        # pulls out the room's sector ID.
        room_value = int(line.strip(all_but_numbers))

    #reads sorted characters, looks for occurrences of all characters
    #in the alphabet. Keeps track of five most frequent occurrences.
        for char in letters:
            if sort_line.count(char) > char_one_num:
                char_five_num, char_five = char_four_num, char_four
                char_four_num, char_four = char_three_num, char_three
                char_three_num, char_three = char_two_num, char_two
                char_two_num, char_two = char_one_num, char_one
                char_one_num, char_one = sort_line.count(char), char
            elif sort_line.count(char) > char_two_num:
                char_five_num, char_five = char_four_num, char_four
                char_four_num, char_four = char_three_num, char_three
                char_three_num, char_three = char_two_num, char_two
                char_two_num, char_two = sort_line.count(char), char
            elif sort_line.count(char) > char_three_num:
                char_five_num, char_five = char_four_num, char_four
                char_four_num, char_four = char_three_num, char_three
                char_three_num, char_three = sort_line.count(char), char
            elif sort_line.count(char) > char_four_num:
                char_five_num, char_five = char_four_num, char_four
                char_four_num, char_four = sort_line.count(char), char
            elif sort_line.count(char) > char_five_num:
                char_five_num, char_five = sort_line.count(char), char

        #the five most common letters, in order
        test = [char_one, char_two, char_three, char_four, char_five]

        # checks to see that test == key. If it is, add room_value to solution.
        for x in range(0, 5):
            if key[x] != test[x]:
                match = False
                break
        if match == True:
            solution += room_value

print solution
