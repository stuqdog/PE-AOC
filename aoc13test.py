def wall_test(x, y):

    check = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + 1362

    check = str(bin(check))
    print check

    one_check = 0

    for c in check:
        if c == "1":
            one_check += 1

    if one_check % 2 == 1:
        print "NOT A WALL"


wall_test(3, 2)
wall_test(4, 1)
wall_test(2, 3)
