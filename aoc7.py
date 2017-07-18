from sys import argv

script, text = argv
solution = 0

with open(text) as f:
    for line in f:
        good_abba = False
        bad_abba = False
        bad_check = None
        good_check = None
        section = "good"

        for char in line:
            if char not in ["[", "]"]:
                if section == "good":
                    bad_check = None
                    if good_check == None:
                        good_check = char
                    else:
                        good_check += char
                elif section == "bad":
                    good_check = None
                    if bad_check == None:
                        bad_check = char
                    else:
                        bad_check += char

            if char == "[":
                section = "bad"
                for x in range(3, len(good_check)):
                    if good_check[x] == good_check[x - 3]:
                        if good_check[x - 1] == good_check[x - 2]:
                            if good_check[x - 1] != good_check[x]:
                                good_abba = True

            if char == "]":
                section = "good"
                for x in range(3, len(bad_check)):
                    if bad_check[x] == bad_check[x - 3]:
                        if bad_check[x - 1] == bad_check[x - 2]:
                            if bad_check[x - 1] != bad_check[x]:
                                bad_abba = True

        if section == "good":
            for x in range(3, len(good_check)):
                if good_check[x] == good_check[x - 3]:
                    if good_check[x - 1] == good_check[x - 2]:
                        if good_check[x - 1] != good_check[x]:
                            good_abba = True

        elif section == "bad":
            for x in range(3, len(bad_check)):
                if bad_check[x] == bad_check[x - 3]:
                    if bad_check[x - 1] == bad_check[x - 2]:
                        if bad_check[x - 1] != bad_check[x]:
                            bad_abba = True

        if good_abba == True and bad_abba == False:
            solution += 1

print solution
