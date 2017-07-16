#1 Set up thing that converts strings to MD5.
#2 create key_base, counter, and key_append
#3 while x != 8, add key append to key_base, convert. If first 5 digits are 0,
  # then add digit 6 to solution, and x += 1
#4 print solution.


import md5

test = md5.new()
solution = " "
x = 0
key_base = "cxdnnyjw"
counter = 0
check_one, check_two, check_three, check_four = False, False, False, False
check_five, check_six, check_seven, check_eight = False, False, False, False


while x != 8:
    success = True
    key_append = str(counter)
    key = key_base + key_append
    test = md5.new(key)
    check = test.hexdigest()
    for y in range(0, 5):
        if check[y] != "0":
            success = False
            break
    print check
    if success == True:
        if check[5] == "0" and check_one == False:
            check_one = True
            solution_one = check[6]
            x += 1
        elif check[5] == "1" and check_two == False:
            check_two = True
            solution_two = check[6]
            x += 1
        if check[5] == "2" and check_three == False:
            check_three = True
            solution_three = check[6]
            x += 1
        elif check[5] == "3" and check_four == False:
            check_four = True
            solution_four = check[6]
            x += 1
        if check[5] == "4" and check_five == False:
            check_five = True
            solution_five = check[6]
            x += 1
        elif check[5] == "5" and check_six == False:
            check_six = True
            solution_six = check[6]
            x += 1
        if check[5] == "6" and check_seven == False:
            check_seven = True
            solution_seven = check[6]
            x += 1
        elif check[5] == "7" and check_eight == False:
            check_eight = True
            solution_eight = check[6]
            x += 1
    counter += 1


solution = solution_one + solution_two + solution_three + solution_four
solution = solution + solution_five + solution_six + solution_seven + solution_eight

print counter
print solution
