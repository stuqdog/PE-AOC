from sys import argv

script, readf = argv

digit = 5


with open(readf) as f:
    while True:
        input = f.read(1)
        if not input:
            break
        if input == "U" and digit > 3:
            digit -= 3
        elif input == "D" and digit < 7:
            digit += 3
        elif input == "L" and digit not in [1, 4, 7]:
            digit -= 1
        elif input == "R" and digit not in [3, 6, 9]:
            digit += 1
        elif input == "V":
            print digit













def formula(digit, input, r_f, digit_num):
    with open(r_f) as f:
        while True:
            input = f.read(1)
            while digit_num < 5:
                if input == "U":
                    if digit > 3:
                        digit -= 3
            #    else:
            #        digit = digit
                elif input == "D":
                    if digit < 7:
                        digit += 3
                #else: digit = digit
                elif input == "L":
                    if digit != 1 and digit != 4 and digit != 7:
                        digit -= 1
                #else:
                #    digit = digit
                elif input == "R":
                    if digit != 3 and digit != 6 and digit != 9:
                        digit += 1
                #else:
                #    digit = digit
                elif input == "V":
                    digit_num += 1
                    print "Digit %d: %d" % digit_num, digit
            if not input:
                break


#with open(readf) as f:
#formula(5, "U", readf, 0)
