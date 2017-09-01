# Circle around, and at each elf check to see if they still have presents.
# if they do, we need to delete elf halfway around.
    #to do that, we could

elf_circle = {}

for x in xrange(0, 3004953):
    elf_circle[x] = True

while len(elf_circle) > 1:
    print len(elf_circle)

    for x in xrange(0, 3004953):
        if x in elf_circle:
            countdown = len(elf_circle) / 2
            for y in xrange(1, 3004953):
                if (x + y) % 3004953 in elf_circle:
                    countdown -= 1

                if countdown == 0:
                    del elf_circle[(x + y) % 3004953]
                    break



            # for y in xrange(1, 3004953):
            #     if (x + y) % 3004953 in elf_circle:
            #         "elf deleted"
            #         del elf_circle[(x + y) % 3004953]
            #         break

for elf in elf_circle:
    print elf + 1
