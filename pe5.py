#Have my solution value. Check if it's divisible by the numbers
#from 1 to 20, one at a time. If it's at any point not divisible by one
#of those numbers, try again.

#Step one: for loop, for x in range(1, 20)
#step two, check if solution is divisible by x.
#if not, break, x+= 1

solution = 22

numbers = [11, 13, 14, 16, 17, 18, 19, 20]

while True:
    for x in numbers:
        if solution % x != 0:
            break
    if solution % x == 0:
        break
    solution += 2
    print "%s\r" % solution,

print solution
