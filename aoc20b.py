import re
ip_list = []
list_size = 0
solution = 0
blocked_ip_upper_bound = 0

with open("aoc20.txt") as f:
    for line in f:
        ip_range = (int(line.split('-')[0]), int(line.rstrip().split('-')[1]))
        ip_list.append(ip_range)
        list_size += 1

ip_list = sorted(ip_list, key=lambda ip_range: ip_range[0])

for i in xrange(0, list_size - 1):
    x = ip_list[i][1] + 1
    if blocked_ip_upper_bound < x:
        blocked_ip_upper_bound = x
    if blocked_ip_upper_bound < ip_list[i + 1][0]:
        solution += (ip_list[i + 1][0] - blocked_ip_upper_bound)

print solution
