from sys import argv

script, direction, ndist, edist, sdist, wdist = argv

distance = 0
ndist = int(ndist)
edist = int(edist)
sdist = int(sdist)
wdist = int(wdist)

dir_mod = raw_input("L or R? ")

if direction == "north" and dir_mod == "L":
    direction = "west"
elif direction == "north" and dir_mod == "R":
    direction = "east"
elif direction == "west" and dir_mod == "L":
    direction = "south"
elif direction == "west" and dir_mod == "R":
    direction = "north"
elif direction == "south" and dir_mod == "L":
    direction = "east"
elif direction == "south" and dir_mod == "R":
    direction = "west"
elif direction == "east" and dir_mod == "L":
    direction = "north"
elif direction == "east" and dir_mod == "R":
    direction = "south"

print "How many blocks?",
distance = int(raw_input())

if direction == "north":
    ndist = ndist + distance
elif direction == "east":
    edist = edist + distance
elif direction == "south":
    sdist = sdist + distance
elif direction == "west":
    wdist = wdist + distance

print """Direction: %s
Distance traveled north: %d
Distance traveled east: %d
Distance traveled south: %d
Distance traveled west: %d""" % (direction, ndist, edist, sdist, wdist)
