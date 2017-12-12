def part_one():
    with open('aoc3.txt') as f:
        triangles = [sorted(line.strip().split(), key=lambda x: int(x)) for line in f]

    return(sum(1 for tri in triangles if int(tri[2]) < (int(tri[1]) + int(tri[0]))))

def part_two():
    with open('aoc3.txt') as f:
        triangles = [line.strip().split() for line in f]
    solution = 0
    tris = [[], [], []]
    for triad in triangles:
        tris[0].append(int(triad[0]))
        tris[1].append(int(triad[1]))
        tris[2].append(int(triad[2]))
        if len(tris[0]) == 3:
            solution += sum(1 for x in tris if sorted(x)[2] < sorted(x)[1] + sorted(x)[0])
            tris = [[], [], []]
    return solution

print(part_one())
print(part_two())
