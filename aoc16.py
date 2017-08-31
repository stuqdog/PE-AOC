def create_dragon(dragon_a):
    dragon_b = []
    for c in reversed(dragon_a):
        if c == 0:
            dragon_b.append(1)
        else:
            dragon_b.append(0)

    dragon_a.append(0)
    dragon_a += dragon_b
    return dragon_a


def create_checksum(input_value):
    check = ''
    for x in range(0, len(input_value), 2):
        if input_value[x] == input_value[x + 1]:
            check += '1'
        else:
            check += '0'
    return check

value = []
start = "01111001100111011"

for c in start:
    if c == '1':
        value.append(1)
    else:
        value.append(0)


while len(value) < 35651584:
    value = create_dragon(value)

value = value[:35651584]
checksum =  create_checksum(value)

while len(checksum) % 2 == 0:
    checksum = create_checksum(checksum)

print checksum
