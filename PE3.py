from sys import exit


# While this was sufficient for the number provided by Project Euler,
# it seems to struggle with numbers where the smallest prime factor is
# particularly large. Is there some way to make this more efficient?

# Step one: find all primes from 2 to sqroot of value.
# Step two: check if value is divisible by those primes, starting from
# the last one

primes = [2]
value = int(raw_input("enter value: \n > "))

solution = value


for iterate in xrange(3, int(value ** .5) + 1, 2): #solution, 2):
    for number in primes:
        if iterate % number == 0:
            break
    if iterate % number != 0:
        primes.append(iterate)
        print "%d\r" % iterate,
        while solution % iterate == 0:
            if solution <= iterate:
                print "Solution is: %d" % solution
                exit(0)
            else:
                solution /= iterate

print "Solution is: %d" % solution





#for number in primes:
#    while solution % number == 0:
#        if solution == number:
#            print solution
#            exit(0)
#        else:
#            solution /= number
#print solution
