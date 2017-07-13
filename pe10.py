


primes = [2]
solution = 2

for x in xrange(3, 2000000, 2):
    for number in primes:
        if x % number == 0:
            break
    if x % number != 0:
        print "%d\r" % x
        solution += x
        primes.append(x)
print solution
