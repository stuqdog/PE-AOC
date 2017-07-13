from sys import exit

primes = [2]
iterate = 1
x = 1

while x <= 10001:
    iterate += 2
    for number in primes:
        if iterate % number == 0:
            break
    if iterate % number != 0:
        primes.append(iterate)
        x += 1
        print "%d.  %d" % (x, iterate)
        if x == 10001:
            exit(0)
