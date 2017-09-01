elf_circle = {}

for x in xrange(0, 3004953):
    elf_circle[x] = True

while len(elf_circle) > 1:
    print len(elf_circle)
    for x in xrange(0, 3004953):
        if x in elf_circle:
            for y in xrange(1, 3004953):
                if (x + y) % 3004953 in elf_circle:
                    "elf deleted"
                    del elf_circle[(x + y) % 3004953]
                    break

for elf in elf_circle:
    print elf + 1
