import re
ip_list = []
list_size = 0

with open("aoc20.txt") as f:
    for line in f:
        ip_range = (int(line.split('-')[0]), int(line.rstrip().split('-')[1]))
        ip_list.append(ip_range)
        list_size += 1

ip_list = sorted(ip_list, key=lambda ip_range: ip_range[0])

#note: this gets the right answer in this case, but won't always. IP ranges can
#overlap, so we could be in the range of ip_list[i-1] but not of [i] or [i+1]

for i in xrange(0, list_size):
    x = ip_list[i][1] + 1
    if x < ip_list[i + 1][0]:
        print x
        break
