elf_circle = {}

for x in xrange(0, 3017957):
    elf_circle[x] = True

while len(elf_circle) > 1:
    print len(elf_circle)
    for x in xrange(0, 3017957):
        if x in elf_circle:
            for y in xrange(1, 3017957):
                if (x + y) % 3017957 in elf_circle:
                    del elf_circle[(x + y) % 3017957]
                    break

for elf in elf_circle:
    print elf + 1
