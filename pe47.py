primes = [2]

current = 3
four_check = 0

while True:
    if all(current % x != 0 for x in primes):
        primes.append(current)
        four_check = 0
    elif sum(1 for x in primes if current % x == 0) == 4:
        four_check += 1
    else:
        four_check = 0

    if four_check == 4:
        break
    current += 1

print(current - 3)
