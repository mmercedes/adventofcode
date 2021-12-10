import string

def read_matrix():
    matrix = []
    with open("./inputs/input_09.txt") as f:
        for line in f:
            matrix.append([int(char) for char in line if char != "\n"])
    return matrix

def is_lowpoint(m, x, y, v):
    width = len(m[0])
    height = len(m)

    # left
    if y > 0 and  m[x][y-1] <= v: return False
    # right
    if y < width-1 and m[x][y+1] <= v: return False
    # up
    if x > 0 and m[x-1][y] <= v: return False
    # down
    if x < height-1 and m[x+1][y] <= v: return False

    return True
    
def p1():
    matrix = read_matrix()
    ans = 0
    lowpoints=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            v = matrix[i][j]
            if is_lowpoint(matrix, i, j, v):
                lowpoints.append((i,j))
                ans += v+1

    print("p1: %i" % ans)
    return (matrix, lowpoints)


def floodfill(m, x0, y0, v):
    width = len(m[0])
    height = len(m)
    queue = [(x0,y0)]

    while len(queue) > 0:
        x,y = queue.pop()

        if m[x][y] != v and m[x][y] != 9:
            m[x][y] = v

            if x > 0:
                queue.append((x-1, y))
            if x < (height-1):
                queue.append((x+1, y))
            if y > 0:
                queue.append((x, y-1))
            if y < (width-1):
                queue.append((x, y+1))
    
def p2(matrix, lowpoints):
    # floodfill starting from each of the lowpoints
    # with a unique int key to distinguish each one
    # then count all instances of the key to determine
    # size of the lowpoints
    for i in range(len(lowpoints)):
        # use negative of lowpoint index as the key for that lowpoint
        # negative to avoid conflicts with original matrix values
        key = -1 - i
        x,y = lowpoints[i]
        floodfill(matrix, x, y, key)

    basin_sizes = {}
    for row in matrix:
        for val in row:
            if val != 9:
                basin_sizes[val] = basin_sizes.get(val, 0)+1

    top3 = sorted(basin_sizes.values())[-3:]
    print("p2: %i" % (top3[0]*top3[1]*top3[2]))

matrix, lowpoints = p1()
p2(matrix, lowpoints)
