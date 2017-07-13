sum_one = sum(x ** 2 for x in range(1, 101))
sum_two = sum(x for x in range(0, 101)) ** 2

print sum_two - sum_one
