
# this is the next number to be added to create a tri_num, which is also which
# entry number the tri num is in the set of tri nums.
tri_num_entry = 1

# our current tri num.
current_tri_num = 0

# set of factors.
factors = []

while True:
    current_tri_num += tri_num_entry
    factors.append(current_tri_num)
    print current_tri_num
    for i in xrange(1, int(current_tri_num ** 0.5 + 1)):
        if current_tri_num % i == 0:
            factors.append(i)
            factors.append(current_tri_num / i)
    if len(factors) > 500:
        print current_tri_num
        print tri_num_entry
        print len(factors)
        break
    factors = []
    tri_num_entry += 1
