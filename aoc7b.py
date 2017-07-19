from sys import argv

script, text = argv
solution = 0

with open(text) as f:
    for line in f:
        aba = {}
        bab = {}
        check_aba = None
        check_bab = None
        section = "aba"
        success = False

        for char in line:
            if char not in ["[", "]"]:
                if section == "aba":
                    if check_aba == None:
                        check_aba = char
                    else:
                        check_aba += char
                elif section == "bab":
                    if check_bab == None:
                        check_bab = char
                    else:
                        check_bab += char

            if char == "[":
                section = "bab"
                if check_aba != None:
                    check_aba += "||"

            if char == "]":
                section = "aba"
                if check_bab != None:
                    check_bab += "||"


        for x in range(2, len(check_aba)):
            if check_aba[x] == check_aba[x - 2] and check_aba[x] != check_aba[x - 1]:
                aba[x] = "%s%s%s" % (check_aba[x], check_aba[x-1], check_aba[x])

        for x in range(2, len(check_bab)):
            if check_bab[x] == check_bab[x - 2] and check_bab[x] != check_bab[x - 1]:
                bab[x] = "%s%s%s" % (check_bab[x], check_bab[x-1], check_bab[x])

        for aba_num, aba_val in aba.items():
            for bab_num, bab_val in bab.items():
                if bab_val[0] == aba_val[1] and bab_val[1] == aba_val[0]:
                    success = True
                    break
            if success == True:
                break

        if success == True:
            solution += 1

print solution
