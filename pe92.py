list_of_winners = {}
solution = 0

for x in range(1, 568):
    check = x
    while check not in [1, 89]:
        test = str(check)
        check = sum(int(i) ** 2 for i in test)
    if check == 89:
        solution += 1
        list_of_winners[x] = 89

for x in range(568, 10000000):
    test = str(x)
    check = sum(int(i) ** 2 for i in test)
    if check in list_of_winners:
        solution += 1

print(solution)
