answer = 0

for x in range(100, 999):
    for y in range(100, 999):
        check = str(x * y)
        if (check[0] == check[-1]) and (check[1] == check[-2]) and (check[2] == check[-3]):
            palindrome = int(check)
            if palindrome > answer:
                answer = palindrome
                factor_one = x
                factor_two = y
print """Answer is: %d.
Factor one is: %d.
Factor two is: %d.""" % (answer, factor_one, factor_two)
