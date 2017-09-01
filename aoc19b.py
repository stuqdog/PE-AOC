# Circle around, and at each elf check to see if they still have presents.
# if they do, we need to delete elf halfway around.
    #to do that, we could

# We could try to put all the elves into a list, delete elf halfway around the list for each
# person until we're done. Problem is the loop. or not. Instead of looping, we could do while True
# and elf number is just constantly iterating. To prevent it from getting longer
# than the list length, we just % it to len(list) and then we do that % starting value.
# Try that with five.

1. One shoots three. (1, 2, 4, 5)
elf_num = 2 (5) = 2. 2 shoots five (1, 2, 4)
elf_num = 3. 3 % 5 is 3, who does go next. 4 eats 1 (2, 4)
elf_num = 4. 4 % 5 = 4.


elf_circle = {}
elf_halfway_around = []

for x in xrange(0, 3004953):
    elf_circle[x] = True
    elf_halfway_around.append(x)

while len(elf_circle) > 1:
    print len(elf_circle)

    for x in xrange(0, 3004953):
        if x in elf_circle:
            countdown = len(elf_circle) / 2
            for y in xrange(1, 3004953):
                if (x + y) % 3004953 in elf_circle:
                    delete_elf = len(elf_circle_list) / 2
                    del elf_circle[elf_halfway_around[delete_elf]]
                    del elf_halfway_around[((len(elf_circle_list) + y) % 3004953)
                    break

                # if countdown == 0:
                #     del elf_circle[(x + y) % 3004953]
                #     break



            # for y in xrange(1, 3004953):
            #     if (x + y) % 3004953 in elf_circle:
            #         "elf deleted"
            #         del elf_circle[(x + y) % 3004953]
            #         break

for elf in elf_circle:
    print elf + 1
