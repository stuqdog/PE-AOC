test = range(0, 10000)

for x in range(0, 10000): #.21 seconds
    # test = [c for i, c in enumerate(test) if i != 0] #6.8 seconds
    #test = test[:-1] #.21 seconds
    #test = [c for c in test if c != 0]
    del test[(10000 - x) / 2] #This is fastest at .06 seconds.

print len(test)
