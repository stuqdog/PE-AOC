# Read lines.
# for each line, divide it into good-abba and bad-abba sections
# to do this, add line[x] to check, one at a time, until line[x] = [
# then, look for an abba. If we find one, then good-abba = True
# then, reset check. add line[x] to check one at a time until line[x] = ]
# then, look for an abba. If we find one, then bad-abba = True.
# as long as bad-abba = false, break, repeat 3 to 6. If it's true, break.
# once line[x] = "\n", we look at bad abba and good abba.
# if good-abba is true and bad-abba is false, solution += 1


from sys import argv
import string

script, text = argv
solution = 0
chars = string.ascii_lowercase
chars += "["
chars += "]"
alphabet = string.ascii_lowercase


with open(text) as f:
    for line in f:
        x = 0
        print line[x]
        good_abba = False
        bad_abba = False
        check = None
        while line[x] in chars:

        # creates a good abba test section
            while good_abba == False:
            #    print line[x]
                if line[x] not in alphabet:
                    break
                elif check == None:
                    check = line[x]
                    x += 1
                else:
                    check += line[x]
                    x += 1

        # checks for good abbas
            if good_abba == False:
                for y in range(3, len(check)):
                    if check[y - 3] == check[y] and check[y - 2] == check[y - 1]:
                        good_abba = True
                        break
            x += 1
            check = None
            print line[x]
            if line[x] not in alphabet:
                break

            # creates a bad abba test section
            while True:
                if line[x] in ("]", "\n"):
                    break
                elif check == None:
                    check = line[x]
                    x += 1
                else:
                    check += line[x]
                    x += 1

            # checks for bad abbas
            for y in range(3, len(check)):
                if check[y - 3] == check[y] and check[y - 2] == check[y - 1]:
                    bad_abba = True
                    break

            x += 1
            check = None
            if line[x] not in chars:
                break

            if bad_abba == True:
                break

        if bad_abba == False and good_abba == True:
            solution += 1

print solution
