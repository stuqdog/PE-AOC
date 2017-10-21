primes = [2]
fractions = 0
for x in range(3, 12001, 2):
    if all(x % i != 0 for i in primes):
        primes.append(x)

for x in range(1, 4000):
    prime_divisors = [i for i in primes if x % i == 0]
    for y in range(x * 2 + 1, x * 3):
        if all(y % i != 0 for i in prime_divisors):
            fractions += 1
for x in range(4000, 6000):
    prime_divisors = [i for i in primes if x % i == 0]
    for y in range(x * 2 + 1, 12001):
        if all(y % i != 0 for i in prime_divisors):
            fractions += 1

print(fractions)
