solution_chain = []
solution = 0

for x in xrange(1, 1000000):
    print x
    chain_length = []
    test_num = x
    while test_num != 1:
        if test_num % 2 == 0:
            test_num /= 2
            chain_length.append(test_num)
        else:
            test_num = test_num * 3 + 1
            chain_length.append(test_num)
    if len(chain_length) > len(solution_chain):
        solution_chain = chain_length
        solution = x

print """The solution is %d.
The chain is %s.
The chain length is %d.""" % (solution, solution_chain, len(solution_chain))
