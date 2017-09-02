seat = 0
elf_circle = range(0, 3004953)
elves = 3004953

while elves > 1:

    if elves % 100000 == 0:
        print elves

    del_elf = (seat + (elves / 2)) % elves
    del elf_circle[del_elf]

    if seat >= elves - 1:
        print elves
        seat = 0
    elif seat + (elves / 2) < elves:
        seat += 1

    elves -= 1




for elf in elf_circle:
    print elf + 1
