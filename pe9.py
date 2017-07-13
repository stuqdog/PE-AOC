# First, we need to generate triplets that sum to 1000.
# Start with the lowest number, a, loop from 1 to 1000 - x
# second number, loop a+1 to 1000
#c = 1000 - a - b
# if c**2 = a**2 + b**2, then print a * b * c and exit


from sys import exit

for a in range(1, 1000):
    for b in range(a + 1, 1000 - a):
        c = 1000 - a - b
        set = [a, b, c]
        test = sorted(set)
        if (test[0] ** 2) + (test[1] ** 2) == test[2] ** 2:
            print a, b, c
            print a * b * c
            exit(0)
