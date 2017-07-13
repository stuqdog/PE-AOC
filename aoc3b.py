from sys import argv

script, test = argv

good_tri = 0
bad_tri = 0
x = 0
triangle_1 = []
triangle_2 = []
triangle_3 = []
limit = 0

with open(test) as f:
    limit_upper = len(f.readlines()) / 3

with open(test) as f:
    # Opportunity for learning. I was able to limit the number of
    # iterations because I knew the length of the file. What if it
    # were variable length? How could I get it to stop running once
    # we reached the end of the file?
    # A: See lines 13 and 14
    while limit < limit_upper:
        while x < 3:
            read_f = f.readline()
            y1, y2, y3 = (int(s) for s in read_f.split())
            triangle_1.append(y1)
            triangle_2.append(y2)
            triangle_3.append(y3)
            x += 1
        tri_sort_1 = sorted(triangle_1)
        tri_sort_2 = sorted(triangle_2)
        tri_sort_3 = sorted(triangle_3)
        if tri_sort_1[0] + tri_sort_1[1] > tri_sort_1[2]:
            good_tri += 1
        else:
            bad_tri += 1
        if tri_sort_2[0] + tri_sort_2[1] > tri_sort_2[2]:
            good_tri += 1
        else:
            bad_tri += 1
        if tri_sort_3[0] + tri_sort_3[1] > tri_sort_3[2]:
            good_tri += 1
        else:
            bad_tri += 1
        triangle_1 = []
        triangle_2 = []
        triangle_3 = []
        limit += 1
        x = 0




print "Possible triangles: %d" % good_tri
print "Impossible triangles: %d" % bad_tri
