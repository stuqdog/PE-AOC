from sys import argv

script, from_file, to_file = argv
openfw = open(to_file, 'w')
openfw.truncate()
openfw.close()

def moven(y_step_n, y_dis_n, x_dis_n, d_istance_n, fw_n, success_n):
    while y_step_n < d_istance_n:
        y_dis_n += 1
        line_n = "%d Y, %d X\n" % (y_dis_n, x_dis_n)
        with open(fw_n, 'r+') as f:
            line_x = f.readlines()
            for line in line_x:
                if line == line_n:
                    print "Success! %s" % line_n
                    success_n = True
            f.write("%d Y, %d X\n" % (y_dis_n, x_dis_n))
        y_step_n += 1
        if success_n == True:
            break
    return y_dis_n, x_dis_n, success_n


def movee(x_step_e, y_dis_e, x_dis_e, distance_e, fw_e, success_e):
    while x_step_e < distance_e:
        x_dis_e += 1
        line_e = "%d Y, %d X\n" % (y_dis_e, x_dis_e)
        with open(fw_e, 'r+') as f:
            line_x = f.readlines()
            for line in line_x:
                if line == line_e:
                    print "Success! %s" % line_e
                    success_e = True
            f.write("%d Y, %d X\n" % (y_dis_e, x_dis_e))
        x_step_e += 1
        if success_e == True:
            break
    return y_dis_e, x_dis_e, success_e


def moves(y_step_s, y_dis_s, x_dis_s, distance_s, fw_s, success_s):
    while y_step_s < distance_s:
        y_dis_s -= 1
        line_sth = "%d Y, %d X\n" % (y_dis_s, x_dis_s)
        with open(fw_s, 'r+') as f:
            line_x = f.readlines()
            for line in line_x:
                if line == line_sth:
                    print "Success! %s" % line_sth
                    success_s = True
            f.write("%d Y, %d X\n" % (y_dis_s, x_dis_s))
        y_step_s += 1
        if success_s == True:
            break
    return y_dis_s, x_dis_s, success_s


def movew(x_step_w, y_dis_w, x_dis_w, distance_w, fw_w, success_w):
    while x_step_w < distance_w:
        x_dis_w -= 1
        line_w = "%d Y, %d X\n" % (y_dis_w, x_dis_w)
        with open(fw_w, 'r+') as f:
            line_x = f.readlines()
            for line in line_x:
                if line == line_w:
                    print "Success! %s" % line_w
                    success_w = True
            f.write("%d Y, %d X\n" % (y_dis_w, x_dis_w))
        x_step_w += 1
        if success_w == True:
            break
    return y_dis_w, x_dis_w, success_w


def steps(fr, fw, direction, xdis, ydis, success):
    dir_mod = fr.readline()
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


    distance = int(fr.readline())

    if direction == "north":
        ydis, xdis, success = moven(0, ydis, xdis, distance, fw, success)
    elif direction == "east":
        ydis, xdis, success = movee(0, ydis, xdis, distance, fw, success)
    elif direction == "south":
        ydis, xdis, success = moves(0, ydis, xdis, distance, fw, success)
    elif direction == "west":
        ydis, xdis, success = movew(0, ydis, xdis, distance, fw, success)






    if success == False:
        steps(fr, fw, direction, xdis, ydis, success)



with open(from_file) as readf:
    steps(readf, to_file, "north", 0, 0, False)
