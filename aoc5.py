#1 Set up thing that converts strings to MD5.
#2 create key_base, counter, and key_append
#3 while x != 8, add key append to key_base, convert. If first 5 digits are 0,
  # then add digit 6 to solution, and x += 1
#4 print solution.


import md5

test = md5.new()
solution = " "
x = 0
key_base = "cxdnnyjw"
counter = 0


while x != 8:
    success = True
    key_append = str(counter)
    key = key_base + key_append
    test = md5.new(key)
    check = test.hexdigest()
    for y in range(0, 5):
        if check[y] != "0":
            success = False
            break
    print check
    if success == True:
        solution += check[5]
        x += 1
    counter += 1


solution = solution.lstrip()

print counter
print solution
