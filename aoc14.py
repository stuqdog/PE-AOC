import md5

class TestHash(object):

    def __init__(self, key_num, key_char):
        self.key_num = key_num
        self.key_char = key_char
        self.countdown = 1000


key_base = "ihaygndm"
key_iterator = 0
triplet_check = []
solution = []

while len(solution) < 64:
    solved_triplets = []
    key = key_base + str(key_iterator)
    test = md5.new(key).hexdigest()

    for i, triplet in enumerate(triplet_check):
        for x in range(0, len(test) - 4):
            if all(test[y] == triplet.key_char for y in range(x, x + 5)):
                solution.append((triplet.key_num, triplet.key_char))
                solved_triplets.append(i)
                print len(solution), solution[-1], key_iterator
        triplet.countdown -= 1
        if triplet.countdown == 0 and i not in solved_triplets:
            solved_triplets.append(i)

    for i in reversed(solved_triplets):
        del triplet_check[i]

    for x in range(0, len(test) - 2):
        if test[x] == test[x + 1] and test[x] == test[x + 2]:
            triplet_check.append(TestHash(key_iterator, test[x]))
            break

    key_iterator += 1

solution = sorted(solution, key=lambda entry: entry[0])
print solution[63], solution[-1]
