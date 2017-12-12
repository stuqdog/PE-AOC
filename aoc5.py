import md5

solution_two =[None] * 8
solution = ''
key_base = "reyedfim"
counter = 0

while any(x == None for x in solution_two):
    key = key_base + str(counter)
    test = md5.new(key).hexdigest()
    if all(test[x] == '0' for x in range(5)):
        solution += test[5]
        if test[5] in ['0', '1', '2', '3', '4', '5', '6', '7']:
            if solution_two[int(test[5])] == None:
                solution_two[int(test[5])] = test[6]
    counter += 1

print("Part one solution: {}".format(solution[:8]))
print("Part two solution: {}".format(''.join(solution_two)))
