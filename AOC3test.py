from sys import argv

script, f = argv

with open(f) as test:
    for line in test:
        for int(s) in line.split:
            n1, n2, n3 = (int(s) for s in line.split())
            print n1, n2, n3
