
from sys import argv

script, file_name = argv

def bite_spot(f, bite):
    f.read()

def jank(direction, distance, ndis, edis, sdis, wdis):
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
        ndis += distance
    elif direction == "east":
        edis += distance
    elif direction == "south":
        sdis += distance
    elif direction == "west":
        wdis += distance

    xdis = edis - wdis
    ydis = ndis - sdis

    print "Currently %d blocks north and %d blocks east" % (ydis, xdis)
    jank(direction, distance, ndis, edis, sdis, wdis)

current_file = open(file_name)

jank("north", 0, 0, 0, 0, 0)
