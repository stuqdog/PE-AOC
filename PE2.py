def PE2(fib1, fib2, fibsum):
    fib2 += fib1
    if fib2 % 2 == 0:
        fibsum += fib2
    fib1 += fib2
    if fib1 % 2 == 0:
        fibsum += fib1
    if fib1 > 4000000:
        print "Sum is %d" % fibsum
    elif fib2 > 4000000:
        print "Sum is %d" % fibsum
    else:
        PE2(fib1, fib2, fibsum)

PE2(1, 1, 0)
