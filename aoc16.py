def main(length):
    a = '10011111011011001'
    while len(a) < length:
        b = ''.join('0' if c == '1' else '1' for c in a)[::-1]
        a = a + '0' + b
    a = a[:length]
    while True:
        check = ''
        for x in range(0, len(a), 2):
            if a[x] == a[x+1]:
                check += '1'
            else:
                check += '0'
        if len(check) % 2 == 1:
            return(check)
        a = check

print(main(272))
print(main(35651584))
