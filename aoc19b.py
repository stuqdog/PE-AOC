# Circle around, and at each elf check to see if they still have presents.
# if they do, we need to delete elf halfway around.
    #to do that, we could

# We could try to put all the elves into a list, delete elf halfway around the list for each
# person until we're done. Problem is the loop. or not. Instead of looping, we could do while True
# and elf number is just constantly iterating. To prevent it from getting larger
# than the list length, we just % it to len(list) and then we do that % starting value.
# Try that with five.

seat = 0

elf_circle = []

for x in xrange(0, 6):#3004953):
    elf_circle.append(x)

elves = len(elf_circle)

while elves > 1:
    # counts around from the seat and deletes elves.
    # elf_circle[:] = [elf in elf_circle if elf !=
    # elf_circle = (elf_circle[:(seat + (elves / 2)) % elves]
    #               + elf_circle[(seat + (elves / 2)) % elves:elves - 1])



    del elf_circle[(seat + (elves / 2)) % elves]
    elves -= 1
    # Need to make seat reset to zero.
    if seat >= elves:
        print elves
        seat = 0
    elif seat < (elves / 2 + 1):
        seat += 1
    #if seat = elves - 1, then we're at the last seat, but we don't want to skip
    #them, which will happen if we add one.
        # We need this to be selective. Only if it deletes an elf who hasn't had
        # their turn yet.
        # if seat < (elves / 2):
        #     seat += 1


    # print len(elf_circle)
    #
    # for x in xrange(0, 3004953):
    #     if x in elf_circle:
    #         countdown = len(elf_circle) / 2
    #         for y in xrange(1, 3004953):
    #             if (x + y) % 3004953 in elf_circle:
    #                 delete_elf = len(elf_circle_list) / 2
    #                 del elf_circle[elf_halfway_around[delete_elf]]
    #                 del elf_halfway_around[((len(elf_circle_list) + y) % 3004953)
    #                 break
    #
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
