import md5
import re

class TestHash(object):

    def __init__(self, key_num, key_char):
        self.key_num = key_num
        self.key_char = key_char
        self.countdown = 1000

key_base = "qzyelonm"
key_iterator = 0
triplet_check = []
solution = []

while len(solution) < 70:
    key = key_base + str(key_iterator)
    test = md5.new(key).hexdigest()
    for x in xrange(2016): # delete this loop to get answer to part one.
        test = md5.new(test).hexdigest()

    for triplet in triplet_check:
        fiver = triplet.key_char * 5
        if fiver in test:
            solution.append(triplet.key_num)
            triplet.countdown = 0
        else:
            triplet.countdown -= 1

    triplet_check = [x for x in triplet_check if x.countdown > 0]

    check = re.search(r'(.)\1\1', test)
    if check:
        triplet_check.append(TestHash(key_iterator, check.group(1)))
    key_iterator += 1
    if key_iterator % 2000 == 0:
        print(key_iterator)

solution = sorted(solution)
print("Part two: {}".format(solution[63]))
