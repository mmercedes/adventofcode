
def read_input():
    width = 0
    height = 0
    points = []
    instructions = []

    with open("./inputs/input_13.txt") as f:
        for line in f:
            if line.startswith("fold along"):
                direction, value = line.split(" ")[-1].strip().split("=")
                instructions.append((direction, int(value)))
            elif not line.strip():
                continue
            else:
                x,y = line.strip().split(",")
                x,y = int(x),int(y)
                if x > width: width = x
                if y > height: height = y
                points.append((x,y))

    width += 1
    height += 1
    matrix = [["." for i in range(width)] for j in range(height)]
    for point in points:
        x,y = point
        matrix[y][x] = "#"

    return (matrix, instructions)

"""
def horizontal_fold(m,l):
    height, width = len(m), len(m[0])
    midpoint = height // 2
    folded = [[0 for i in range(width)] for j in range(midpoint)]
    if l != midpoint: 
        print("H ya dun goofed, mid: %i l: %i" % (midpoint, l))    
    for x in range(width):
        for y in range(midpoint):
            p1 = m[y][x]
            p2 = m[height - y - 1][x]
            if p1 == "#" or p2 == "#":
                folded[y][x] = "#"
            else:
                folded[y][x] = "."            

    return folded
"""

def horizontal_fold(m, l):
    height, width = len(m), len(m[0])
    m1 = [[m[j][i] for i in range(width)] for j in range(l)]
    m2 = [[m[j][i] for i in range(width)] for j in range(l+1, height)]

    if len(m1) >= len(m2):
        midy = len(m1)
        for y in range(len(m2)):
            for x in range(width):
                if m2[y][x] == "#":
                    m1[midy-y-1][x] = "#"       
    return m1
    
def vertical_fold(m,l):
    height, width = len(m), len(m[0])
    midpoint = width // 2
    folded = [[0 for i in range(midpoint)] for j in range(height)]

    for y in range(height):
        for x in range(midpoint):
            p1 = m[y][x]
            p2 = m[y][width - x - 1]
            if p1 == "#" or p2 == "#":
                folded[y][x] = "#"
            else:
                folded[y][x] = "."

    return folded

"""
ex = [
    ['#','.','#','#','.','.','#','.','.','#','.'],
    ['#','.','.','.','#','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','#','.','.','.','#'],
    ['#','.','.','.','#','.','.','.','.','.','.'],
    ['.','#','.','#','.','.','#','.','#','#','#'],
    ['.','.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.','.','.','.']]

res = vertical_fold(ex, 0)
for r in res:
    print(str(r))
"""
"""
ex = [
    ['.','.','.','#','.','.','#','.','.','#','.'],
    ['.','.','.','.','#','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.'],
    ['#','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','#','.','.','.','.','#','.','#'],
    ['.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.'],
    ['-','-','-','-','-','-','-','-','-','-','-'],
    ['.','.','.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.','.','.'],
    ['.','#','.','.','.','.','#','.','#','#','.'],
    ['.','.','.','.','#','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','#','.','.','.','#'],
    ['#','.','.','.','.','.','.','.','.','.','.'],
    ['#','.','#','.','.','.','.','.','.','.','.']]

res = horizontal_fold2(ex, 7)
for r in res:
    print("".join(r))
"""

def p1():
    (matrix, instructions) = read_input()
    m = vertical_fold(matrix, 0)
    ans = 0
    for row in m:
        for item in row:
            if item == "#":
                ans += 1
    print("p1: %i" % ans)

def p2():
    (matrix, instructions) = read_input()
    for ins in instructions:
        (axis, l) = ins
        if axis == "x":
            matrix = vertical_fold(matrix,l)
        else:
            matrix = horizontal_fold2(matrix,l)

    for r in matrix:
        print("".join(r))
    return

p1()
p2()
