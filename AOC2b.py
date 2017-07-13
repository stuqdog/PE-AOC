from sys import argv

script, readf = argv

digit = 5


with open(readf) as f:
    while True:
        input = f.read(1)
        if not input:
            break
        if input == "U":
            if digit == 3:
                digit = 1
            elif digit in [6, 7, 8]:
                digit -= 4
            elif digit == "A":
                digit = 6
            elif digit == "B":
                digit = 7
            elif digit == "C":
                digit = 8
            elif digit == "D":
                digit = "B"
        elif input == "D":
            if digit == 1:
                digit = 3
            elif digit in [2, 3, 4]:
                digit += 4
            elif digit == 6:
                digit = "A"
            elif digit == 7:
                digit = "B"
            elif digit == 8:
                digit = "C"
            elif digit == "B":
                digit = "D"
        elif input == "L":
            if digit in [3, 4, 6, 7, 8, 9]:
                digit -= 1
            elif digit == "B":
                digit = "A"
            elif digit == "C":
                digit = "B"
        elif input == "R":
            if digit in [2, 3, 5, 6, 7, 8]:
                digit += 1
            elif digit == "A":
                digit = "B"
            elif digit == "B":
                digit = "C"
        elif input == "V":
            print digit
