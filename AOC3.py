from sys import argv

script, test = argv

good_tri = 0
bad_tri = 0
x = 0
triangle = []

with open(test) as f:
    for line in f:
#        for s in line.split():
#            y = int(s)
        y1, y2, y3 = (int(s) for s in line.split())
        triangle.append(y1)
        triangle.append(y2)
        triangle.append(y3)
        #        x += 1
        tri_sort = sorted(triangle)
        if tri_sort[0] + tri_sort[1] > tri_sort[2]:
            good_tri += 1
        else:
            bad_tri += 1
        triangle = []
print "Possible triangles: %d" % good_tri
print "Impossible triangles: %d" % bad_tri
