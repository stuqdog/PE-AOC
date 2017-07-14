#1. set loop to repeat for each line. DONE
#2. Read the line, remove 5 letter key at the end and the room code. DONE
#3. Sort line. DONE
#4. Remove '-' from line.
#5. Sort line by most common occurrence, then delete duplicates.
#6. Compare sorted line to 5 letter key.
#7 If sorted line and 5 letter key match, add room code to sum.
#2 read the line, parsing at -. add letters before numbers to check set,
#  add letter after numbers to key set. Add letters to check_sum set.
#3 sort check set by most common appearance, remove duplicates.
#4 see if check[x] = key[x] for x in range(0, 5). If it does, then
#  add check_sum to solution.



from sys import argv
import string

letters = string.ascii_letters
numbers = string.digits
first_strip = "%s[]\n" % letters


script, text = argv

with open(text) as f:
    for line in f:
        sort_line = line.rstrip(first_strip)
        sort_line = sort_line.rstrip(numbers)
        sort_line = sorted(sort_line)
        print sort_line
