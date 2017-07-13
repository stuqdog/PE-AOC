
from sys import argv

script, file_name = argv




def jank(direction, distance, ndis, edis, sdis, wdis, f, line):

    dir_mod = f.readline()
    line += 1
    if direction == "north" and dir_mod == "L\n":
        direction = "west"
    elif direction == "north" and dir_mod == "R\n":
        direction = "east"
    elif direction == "west" and dir_mod == "L\n":
        direction = "south"
    elif direction == "west" and dir_mod == "R\n":
        direction = "north"
    elif direction == "south" and dir_mod == "L\n":
        direction = "east"
    elif direction == "south" and dir_mod == "R\n":
        direction = "west"
    elif direction == "east" and dir_mod == "L\n":
        direction = "north"
    elif direction == "east" and dir_mod == "R\n":
        direction = "south"


    distance = int(f.readline())
    line += 1

    if direction == "north":
        ndis += distance
    elif direction == "east":
        edis += distance
    elif direction == "south":
        sdis += distance
    elif direction == "west":
        wdis += distance

    if line >= 388:
        print """Traveled:
        * %d blocks N
        * %d blocks E,
        * %d blocks S, and
        * %d blocks W""" % (ndis, edis, sdis, wdis)
    else:
        jank(direction, distance, ndis, edis, sdis, wdis, f, line)

current_file = open(file_name)

current_file.seek(0)

jank("north", 0, 0, 0, 0, 0, current_file, 0)
