fib_one = 1
fib_two = 1
fib_term = 2


while True:
    fib_one, fib_two = fib_one + fib_two, fib_one
    fib_term += 1

    if len(str(fib_one)) == 1000:
        print fib_term
        break
