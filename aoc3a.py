from sys import argv

script, file = argv

with open(file) as f:
    print len(f.readlines())
