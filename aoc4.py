#1. set loop to repeat a number of times equal to the # of lines. DONE
#2 read the line, parsing at -. add letters before numbers to check set,
#  add letter after numbers to key set. Add letters to check_sum set.
#3 sort check set by most common appearance, remove duplicates.
#4 see if check[x] = key[x] for x in range(0, 5). If it does, then
#  add check_sum to solution.


from sys import argv

script, text = argv

with open(text) as f:
    loop_number = len(f.readlines())

with open(text) as f:
    for x in range(0, 3):
        loop = f.readline()
        #loop_parsed = loop[0]
        print loop
        #print loop_parsed
